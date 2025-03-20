from machine import Pin,ExtInt
from misc import ADC,PWM_V2
import utime



# 硬件初始化
adc = ADC()    # 旋钮接ADC0
led = Pin(Pin.GPIO6,Pin.OUT,Pin.PULL_DISABLE,1)  # LED接GPIO6
pwm = PWM_V2(PWM_V2.PWM0,100.0,100)

# 主循环读取ADC并更新占空比
def Knob_light():
    """
    主循环读取ADC值并根据ADC值更新PWM占空比，用于控制灯光亮度。
    该函数在`Mode`为`True`时持续运行，读取ADC值并将其转换为占空比，然后更新PWM输出。
    占空比的范围被限制在5%到100%之间，以避免完全关闭或完全打开的情况。
    """
    while Mode:
        # 读取ADC值（0-1199）
        adc.open()
        adc_val = adc.read(ADC.ADC0)
        #print("ADC Value:", adc_val)
        # 转换为0-100的占空比（保留5%死区）
        new_duty = int((adc_val / 1600) * 95) + 5
        
        # 更新占空比
        if new_duty > 5 and new_duty < 100:
            duty_cycle =new_duty # 限制在5-100%范围
            pwm.open(100.0,duty_cycle)
        elif new_duty <= 5:
            duty_cycle = 5
            pwm.open(100.0,duty_cycle)
        elif new_duty >= 100:
            duty_cycle = 100
            pwm.open(100.0,duty_cycle)
        #print("Duty Cycle:", duty_cycle)
        utime.sleep_ms(50)  # 降低采样频率，避免过于频繁的更新
def Breath_light():
    """
    呼吸灯效果函数。
    该函数通过循环调整PWM占空比，实现LED灯的呼吸效果。函数会持续运行，直到`Mode`变量为真。
    占空比从0逐渐增加到99，然后再从100逐渐减少到1，形成呼吸灯的效果。

    """
    while not Mode:
        # 逐渐增加占空比，使LED灯逐渐变亮
        for duty in range(0, 99, 1):
            pwm.open(100.0,duty)
            utime.sleep_ms(10)
        
        # 逐渐减少占空比，使LED灯逐渐变暗
        for duty in range(100, 1, -1):
            pwm.open(100.0,duty)
            utime.sleep_ms(10)

Mode = False
def key_call_back(args):
    """
    按键中断回调函数。
    该函数在按键按下时调用，用于切换LED灯的模式。
    """
    global Mode
    Mode = not Mode
    print("Mode changed")
    utime.sleep_ms(20)

key_extint = ExtInt(ExtInt.GPIO4, ExtInt.IRQ_RISING, ExtInt.PULL_PU, key_call_back)
key_extint.enable()


if __name__ == '__main__':
    try:
        while True:
            if not Mode:
                Breath_light()
            else:
                Knob_light()
    except KeyboardInterrupt:
        led.write(0)  # 关闭LED
        pwm.close()
        key_extint.disable()
        print("Program exited")
