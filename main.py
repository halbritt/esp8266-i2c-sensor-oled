import machine
import bme280
import mcp9808
import ssd1306


i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
bme = bme280.BME280(i2c=i2c)
mcp9808 = mcp9808.MCP9808(i2c=i2c)

print(bme.values)
mcp9808.get_temp()

