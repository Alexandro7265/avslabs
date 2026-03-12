import struct

def binary16_to_float(hex_or_bytes):
    if isinstance(hex_or_bytes, str):
        if hex_or_bytes.startswith('0x'):
            hex_or_bytes = hex_or_bytes[2:]  
        byte_data = bytes.fromhex(hex_or_bytes)
    else:
        byte_data = hex_or_bytes
    float_value, = struct.unpack('<e', byte_data)
    return float_value


hex_input = "0x4000" 
result = binary16_to_float(hex_input)
print(f"Десятичное значение: {result}")
