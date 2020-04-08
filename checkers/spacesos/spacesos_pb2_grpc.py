# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import spacesos_pb2 as spacesos__pb2


class SpaceSosStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Register = channel.unary_unary(
        '/spacesos.SpaceSos/Register',
        request_serializer=spacesos__pb2.AuthRequest.SerializeToString,
        response_deserializer=spacesos__pb2.AuthResponse.FromString,
        )
    self.Login = channel.unary_unary(
        '/spacesos.SpaceSos/Login',
        request_serializer=spacesos__pb2.AuthRequest.SerializeToString,
        response_deserializer=spacesos__pb2.AuthResponse.FromString,
        )
    self.AddToFriend = channel.unary_unary(
        '/spacesos.SpaceSos/AddToFriend',
        request_serializer=spacesos__pb2.AddToFriendRequest.SerializeToString,
        response_deserializer=spacesos__pb2.AddToFriendResponse.FromString,
        )
    self.FriendshipRequests = channel.unary_unary(
        '/spacesos.SpaceSos/FriendshipRequests',
        request_serializer=spacesos__pb2.FriendshipRequestsRequest.SerializeToString,
        response_deserializer=spacesos__pb2.FriendshipRequestResponse.FromString,
        )
    self.GetFriends = channel.unary_unary(
        '/spacesos.SpaceSos/GetFriends',
        request_serializer=spacesos__pb2.FriendsRequest.SerializeToString,
        response_deserializer=spacesos__pb2.FriendsResponse.FromString,
        )
    self.Crash = channel.unary_unary(
        '/spacesos.SpaceSos/Crash',
        request_serializer=spacesos__pb2.CrashRequest.SerializeToString,
        response_deserializer=spacesos__pb2.CrashResponse.FromString,
        )
    self.GetCrashes = channel.unary_unary(
        '/spacesos.SpaceSos/GetCrashes',
        request_serializer=spacesos__pb2.GetCrashesRequest.SerializeToString,
        response_deserializer=spacesos__pb2.GetCrashesResponse.FromString,
        )
    self.GetLatestCrashes = channel.unary_unary(
        '/spacesos.SpaceSos/GetLatestCrashes',
        request_serializer=spacesos__pb2.GetLatestCrashesRequest.SerializeToString,
        response_deserializer=spacesos__pb2.GetLatestCrashesResponse.FromString,
        )


class SpaceSosServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Register(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Login(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddToFriend(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FriendshipRequests(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetFriends(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Crash(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetCrashes(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetLatestCrashes(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SpaceSosServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Register': grpc.unary_unary_rpc_method_handler(
          servicer.Register,
          request_deserializer=spacesos__pb2.AuthRequest.FromString,
          response_serializer=spacesos__pb2.AuthResponse.SerializeToString,
      ),
      'Login': grpc.unary_unary_rpc_method_handler(
          servicer.Login,
          request_deserializer=spacesos__pb2.AuthRequest.FromString,
          response_serializer=spacesos__pb2.AuthResponse.SerializeToString,
      ),
      'AddToFriend': grpc.unary_unary_rpc_method_handler(
          servicer.AddToFriend,
          request_deserializer=spacesos__pb2.AddToFriendRequest.FromString,
          response_serializer=spacesos__pb2.AddToFriendResponse.SerializeToString,
      ),
      'FriendshipRequests': grpc.unary_unary_rpc_method_handler(
          servicer.FriendshipRequests,
          request_deserializer=spacesos__pb2.FriendshipRequestsRequest.FromString,
          response_serializer=spacesos__pb2.FriendshipRequestResponse.SerializeToString,
      ),
      'GetFriends': grpc.unary_unary_rpc_method_handler(
          servicer.GetFriends,
          request_deserializer=spacesos__pb2.FriendsRequest.FromString,
          response_serializer=spacesos__pb2.FriendsResponse.SerializeToString,
      ),
      'Crash': grpc.unary_unary_rpc_method_handler(
          servicer.Crash,
          request_deserializer=spacesos__pb2.CrashRequest.FromString,
          response_serializer=spacesos__pb2.CrashResponse.SerializeToString,
      ),
      'GetCrashes': grpc.unary_unary_rpc_method_handler(
          servicer.GetCrashes,
          request_deserializer=spacesos__pb2.GetCrashesRequest.FromString,
          response_serializer=spacesos__pb2.GetCrashesResponse.SerializeToString,
      ),
      'GetLatestCrashes': grpc.unary_unary_rpc_method_handler(
          servicer.GetLatestCrashes,
          request_deserializer=spacesos__pb2.GetLatestCrashesRequest.FromString,
          response_serializer=spacesos__pb2.GetLatestCrashesResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'spacesos.SpaceSos', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
