'''
Created on Oct 1, 2011

@author: kinow
'''
import xmlrpclib

class XMLRPCIC:
    
    def __init__(self, serverURL):
        self.serverURL = serverURL
        
    def getServerURL(self):
        return self.serverURL
    
    def getServer(self):
        return xmlrpclib.Server(self.serverURL)
    
    def getAvailableMethods(self):
        return self.getServer().system.listMethods()
    
    def getMethodSignature(self, methodName):
        return self.getServer().system.getCapabilities()

if __name__ == '__main__':
    client = XMLRPCIC('http://localhost/testlink-1.9.3/lib/api/xmlrpc.php');
    
    methods = client.getAvailableMethods()
    print methods
    
    sign = client.getMethodSignature('tl.setTestCaseExecutionResult')
    
    print sign
    
    