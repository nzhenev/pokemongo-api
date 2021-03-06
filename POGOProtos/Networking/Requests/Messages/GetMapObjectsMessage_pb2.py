# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos/Networking/Requests/Messages/GetMapObjectsMessage.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='POGOProtos/Networking/Requests/Messages/GetMapObjectsMessage.proto',
  package='POGOProtos.Networking.Requests.Messages',
  syntax='proto3',
  serialized_pb=_b('\nBPOGOProtos/Networking/Requests/Messages/GetMapObjectsMessage.proto\x12\'POGOProtos.Networking.Requests.Messages\"p\n\x14GetMapObjectsMessage\x12\x13\n\x07\x63\x65ll_id\x18\x01 \x03(\x04\x42\x02\x10\x01\x12\x1e\n\x12since_timestamp_ms\x18\x02 \x03(\x03\x42\x02\x10\x01\x12\x10\n\x08latitude\x18\x03 \x01(\x01\x12\x11\n\tlongitude\x18\x04 \x01(\x01\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_GETMAPOBJECTSMESSAGE = _descriptor.Descriptor(
  name='GetMapObjectsMessage',
  full_name='POGOProtos.Networking.Requests.Messages.GetMapObjectsMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cell_id', full_name='POGOProtos.Networking.Requests.Messages.GetMapObjectsMessage.cell_id', index=0,
      number=1, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
    _descriptor.FieldDescriptor(
      name='since_timestamp_ms', full_name='POGOProtos.Networking.Requests.Messages.GetMapObjectsMessage.since_timestamp_ms', index=1,
      number=2, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='POGOProtos.Networking.Requests.Messages.GetMapObjectsMessage.latitude', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='POGOProtos.Networking.Requests.Messages.GetMapObjectsMessage.longitude', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=111,
  serialized_end=223,
)

DESCRIPTOR.message_types_by_name['GetMapObjectsMessage'] = _GETMAPOBJECTSMESSAGE

GetMapObjectsMessage = _reflection.GeneratedProtocolMessageType('GetMapObjectsMessage', (_message.Message,), dict(
  DESCRIPTOR = _GETMAPOBJECTSMESSAGE,
  __module__ = 'POGOProtos.Networking.Requests.Messages.GetMapObjectsMessage_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Networking.Requests.Messages.GetMapObjectsMessage)
  ))
_sym_db.RegisterMessage(GetMapObjectsMessage)


_GETMAPOBJECTSMESSAGE.fields_by_name['cell_id'].has_options = True
_GETMAPOBJECTSMESSAGE.fields_by_name['cell_id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_GETMAPOBJECTSMESSAGE.fields_by_name['since_timestamp_ms'].has_options = True
_GETMAPOBJECTSMESSAGE.fields_by_name['since_timestamp_ms']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
# @@protoc_insertion_point(module_scope)
