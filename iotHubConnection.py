from azure.iot.device.aio import IoTHubDeviceClient

class IoTHubConnection:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.client = None

    async def connect(self):
        self.client = IoTHubDeviceClient.create_from_connection_string(self.connection_string)
        await self.client.connect()

    async def disconnect(self):
        if self.client:
            await self.client.disconnect()
            self.client = None

    async def send_message(self, message):
        if self.client:
            await self.client.send_message(message)
            print("Message sent: ", message)
        else:
            print("Client not connected. Cannot send message.")