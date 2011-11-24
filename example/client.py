import jsonrpc

server = jsonrpc.Server("http://localhost:6996/rpc")
print server.test_add(23, 3)
print server.foo()

