import socket

def servlookup(startPortRange=80, endPortRange=90):
    '''takes a range of valid ports and returns the services
        provided by those ports
    '''
    if int(endPortRange) > 65535:
        return "Please specify a valid endPortRange"

    if int(startPortRange) < 0:
        return "Please specify a valid startPortRange"

    ports = range(int(startPortRange), (int(endPortRange) + 1))

    for k in ports:
        try:
            service = socket.getservbyport(k)
            print 'port {0} serves {1}'.format(k, service)
        except socket.error:
            print 'port {0} not found'.format(k)