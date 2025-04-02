import grpc
from grpc_utils.tensor_transmit import TensorTransmit_pb2
from grpc_utils.tensor_transmit import TensorTransmit_pb2_grpc
import torch
from concurrent import futures
import numpy as np
import logging

activation_list = [torch.rand((197, 768)) for i in range(12)]

class TensorTransmit(TensorTransmit_pb2_grpc.TensorTransmitServicer):
    def GetActivationFloat(self, request, context):
        tensor = activation_list[request]
        return TensorTransmit_pb2.ActivationFloat(data=tensor.flatten().tolist(), shape_f=tensor.shape)

    def GetActivationByte(self, request, context):
        tensor = activation_list[request]
        return TensorTransmit_pb2.ActivationByte(buffer=tensor.cpu().numpy().tobytes(),
                                                 shape_b=tensor.shape,
                                                 dtype=tensor.cpu().numpy().dtype
                                                 )

def serve():
    port = "50052"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    TensorTransmit_pb2_grpc.add_TensorTransmitServicer_to_server(TensorTransmit, server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on port " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()

