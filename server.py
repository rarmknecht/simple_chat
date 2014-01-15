#!/usr/bin/python
from twisted.internet import protocol, reactor

# TODO - Multi-threaded support
# TODO - Port as command line option
# TODO - Scheme for targets of messages
# TODO - Queue of messages received
# TODO - Message Polling from Clients


class Echo(protocol.Protocol):
    def dataReceived(self, data):
        self.transport.write(data)

class EchoFactory(protocol.Factory):
    def buildProtocol(self,addr):
        return Echo()

if __name__ == "__main__":
    reactor.listenTCP(5151, EchoFactory())
    reactor.run()
