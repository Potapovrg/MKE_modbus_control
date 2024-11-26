from pymodbus.client import ModbusTcpClient
import time

# Device settings
ip_address = '192.168.0.10'
port = 5000
slave_id = 1

# Function code (06 - Write Single Register)
function_code = 6

# Relay commands
relay_on_command = 0x0100
relay_off_command = 0x0200

def control_relay(client, relay_number, command):
    """
    Controls the specified relay by sending a Modbus write command.
    
    Parameters:
    client - The Modbus TCP client
    relay_number - The relay number (1 to 12)
    command - The command to turn on (0x0100) or off (0x0200) the relay
    """
    address = relay_number - 1  # Assuming relay addresses are sequential
    response = client.write_register(address, command, slave=slave_id)
    
    if response.isError():
        print(f"Error controlling relay {relay_number}")
    else:
        print(f"Relay {relay_number} successfully controlled")

# Main logic
if __name__ == "__main__":
    # Connect to Modbus TCP device
    client = ModbusTcpClient(ip_address, port=port)
    
    if client.connect():
        # Loop through each relay (1 to 12)
        for relay in range(1, 13):
            # Turn on the relay
            control_relay(client, relay, relay_on_command)
            time.sleep(3)  # Keep it on for 1 second
            
            # Turn off the relay
            control_relay(client, relay, relay_off_command)
            time.sleep(0.5)  # Wait a moment before moving to the next relay
        
        # Close connection
        client.close()
    else:
        print("Unable to connect to Modbus TCP device")