import logging
import grpc
from grpc_utils.tensor_transmit import TensorTransmit_pb2
from grpc_utils.tensor_transmit import TensorTransmit_pb2_grpc


def run(ip_addr, port, layer_index):
    print("try to grab tensor from server ...")
    with grpc.insecure_channel(ip_addr + ":" + port) as channel:
        stub = TensorTransmit_pb2_grpc.TensorTransmitStub(channel)
        response = stub.GetActivationFloat(TensorTransmit_pb2.Layer(layer_index=layer_index))
    print("Received tensor is: ", response.message)


if __name__ == "__main__":
    ip_addr = input("Enter the ip address of the server: ")
    port = input("Enter the port number on the server: ")
    layer = input("Enter the index of the layer you want to grab the tensor in: ")
    logging.basicConfig()
    run(ip_addr, port, layer)

