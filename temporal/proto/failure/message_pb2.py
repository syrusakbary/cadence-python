# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: temporal/proto/failure/message.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='temporal/proto/failure/message.proto',
  package='failure',
  syntax='proto3',
  serialized_options=b'\n\031io.temporal.proto.failureP\001Z%go.temporal.io/temporal-proto/failure',
  serialized_pb=b'\n$temporal/proto/failure/message.proto\x12\x07\x66\x61ilure\"9\n\x08NotFound\x12\x16\n\x0e\x63urrentCluster\x18\x01 \x01(\t\x12\x15\n\ractiveCluster\x18\x02 \x01(\t\"H\n\x1fWorkflowExecutionAlreadyStarted\x12\x16\n\x0estartRequestId\x18\x01 \x01(\t\x12\r\n\x05runId\x18\x02 \x01(\t\"V\n\x12NamespaceNotActive\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x16\n\x0e\x63urrentCluster\x18\x02 \x01(\t\x12\x15\n\ractiveCluster\x18\x03 \x01(\t\"X\n\tRetryTask\x12\x13\n\x0bnamespaceId\x18\x01 \x01(\t\x12\x12\n\nworkflowId\x18\x02 \x01(\t\x12\r\n\x05runId\x18\x03 \x01(\t\x12\x13\n\x0bnextEventId\x18\x04 \x01(\x03\"\xa3\x01\n\x0bRetryTaskV2\x12\x13\n\x0bnamespaceId\x18\x01 \x01(\t\x12\x12\n\nworkflowId\x18\x02 \x01(\t\x12\r\n\x05runId\x18\x03 \x01(\t\x12\x14\n\x0cstartEventId\x18\x04 \x01(\x03\x12\x19\n\x11startEventVersion\x18\x05 \x01(\x03\x12\x12\n\nendEventId\x18\x06 \x01(\x03\x12\x17\n\x0f\x65ndEventVersion\x18\x07 \x01(\x03\"a\n\x19\x43lientVersionNotSupported\x12\x15\n\rclientVersion\x18\x01 \x01(\t\x12\x12\n\nclientImpl\x18\x02 \x01(\t\x12\x19\n\x11supportedVersions\x18\x03 \x01(\t\"`\n\x1a\x46\x65\x61tureVersionNotSupported\x12\x0f\n\x07\x66\x65\x61ture\x18\x01 \x01(\t\x12\x16\n\x0e\x66\x65\x61tureVersion\x18\x02 \x01(\t\x12\x19\n\x11supportedVersions\x18\x03 \x01(\t\"2\n\x14\x43urrentBranchChanged\x12\x1a\n\x12\x63urrentBranchToken\x18\x01 \x01(\x0c\"#\n\x12ShardOwnershipLost\x12\r\n\x05owner\x18\x01 \x01(\t\"\x18\n\x16NamespaceAlreadyExists\"\x1e\n\x1c\x43\x61ncellationAlreadyRequested\"\r\n\x0bQueryFailed\"\x15\n\x13\x45ventAlreadyStartedBD\n\x19io.temporal.proto.failureP\x01Z%go.temporal.io/temporal-proto/failureb\x06proto3'
)




_NOTFOUND = _descriptor.Descriptor(
  name='NotFound',
  full_name='failure.NotFound',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='currentCluster', full_name='failure.NotFound.currentCluster', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='activeCluster', full_name='failure.NotFound.activeCluster', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=49,
  serialized_end=106,
)


_WORKFLOWEXECUTIONALREADYSTARTED = _descriptor.Descriptor(
  name='WorkflowExecutionAlreadyStarted',
  full_name='failure.WorkflowExecutionAlreadyStarted',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='startRequestId', full_name='failure.WorkflowExecutionAlreadyStarted.startRequestId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='runId', full_name='failure.WorkflowExecutionAlreadyStarted.runId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=108,
  serialized_end=180,
)


_NAMESPACENOTACTIVE = _descriptor.Descriptor(
  name='NamespaceNotActive',
  full_name='failure.NamespaceNotActive',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='namespace', full_name='failure.NamespaceNotActive.namespace', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='currentCluster', full_name='failure.NamespaceNotActive.currentCluster', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='activeCluster', full_name='failure.NamespaceNotActive.activeCluster', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=182,
  serialized_end=268,
)


_RETRYTASK = _descriptor.Descriptor(
  name='RetryTask',
  full_name='failure.RetryTask',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='namespaceId', full_name='failure.RetryTask.namespaceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='workflowId', full_name='failure.RetryTask.workflowId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='runId', full_name='failure.RetryTask.runId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nextEventId', full_name='failure.RetryTask.nextEventId', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=270,
  serialized_end=358,
)


_RETRYTASKV2 = _descriptor.Descriptor(
  name='RetryTaskV2',
  full_name='failure.RetryTaskV2',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='namespaceId', full_name='failure.RetryTaskV2.namespaceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='workflowId', full_name='failure.RetryTaskV2.workflowId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='runId', full_name='failure.RetryTaskV2.runId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='startEventId', full_name='failure.RetryTaskV2.startEventId', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='startEventVersion', full_name='failure.RetryTaskV2.startEventVersion', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='endEventId', full_name='failure.RetryTaskV2.endEventId', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='endEventVersion', full_name='failure.RetryTaskV2.endEventVersion', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=361,
  serialized_end=524,
)


_CLIENTVERSIONNOTSUPPORTED = _descriptor.Descriptor(
  name='ClientVersionNotSupported',
  full_name='failure.ClientVersionNotSupported',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='clientVersion', full_name='failure.ClientVersionNotSupported.clientVersion', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clientImpl', full_name='failure.ClientVersionNotSupported.clientImpl', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='supportedVersions', full_name='failure.ClientVersionNotSupported.supportedVersions', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=526,
  serialized_end=623,
)


_FEATUREVERSIONNOTSUPPORTED = _descriptor.Descriptor(
  name='FeatureVersionNotSupported',
  full_name='failure.FeatureVersionNotSupported',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='feature', full_name='failure.FeatureVersionNotSupported.feature', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='featureVersion', full_name='failure.FeatureVersionNotSupported.featureVersion', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='supportedVersions', full_name='failure.FeatureVersionNotSupported.supportedVersions', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=625,
  serialized_end=721,
)


_CURRENTBRANCHCHANGED = _descriptor.Descriptor(
  name='CurrentBranchChanged',
  full_name='failure.CurrentBranchChanged',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='currentBranchToken', full_name='failure.CurrentBranchChanged.currentBranchToken', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=723,
  serialized_end=773,
)


_SHARDOWNERSHIPLOST = _descriptor.Descriptor(
  name='ShardOwnershipLost',
  full_name='failure.ShardOwnershipLost',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='owner', full_name='failure.ShardOwnershipLost.owner', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=775,
  serialized_end=810,
)


_NAMESPACEALREADYEXISTS = _descriptor.Descriptor(
  name='NamespaceAlreadyExists',
  full_name='failure.NamespaceAlreadyExists',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=812,
  serialized_end=836,
)


_CANCELLATIONALREADYREQUESTED = _descriptor.Descriptor(
  name='CancellationAlreadyRequested',
  full_name='failure.CancellationAlreadyRequested',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=838,
  serialized_end=868,
)


_QUERYFAILED = _descriptor.Descriptor(
  name='QueryFailed',
  full_name='failure.QueryFailed',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=870,
  serialized_end=883,
)


_EVENTALREADYSTARTED = _descriptor.Descriptor(
  name='EventAlreadyStarted',
  full_name='failure.EventAlreadyStarted',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=885,
  serialized_end=906,
)

DESCRIPTOR.message_types_by_name['NotFound'] = _NOTFOUND
DESCRIPTOR.message_types_by_name['WorkflowExecutionAlreadyStarted'] = _WORKFLOWEXECUTIONALREADYSTARTED
DESCRIPTOR.message_types_by_name['NamespaceNotActive'] = _NAMESPACENOTACTIVE
DESCRIPTOR.message_types_by_name['RetryTask'] = _RETRYTASK
DESCRIPTOR.message_types_by_name['RetryTaskV2'] = _RETRYTASKV2
DESCRIPTOR.message_types_by_name['ClientVersionNotSupported'] = _CLIENTVERSIONNOTSUPPORTED
DESCRIPTOR.message_types_by_name['FeatureVersionNotSupported'] = _FEATUREVERSIONNOTSUPPORTED
DESCRIPTOR.message_types_by_name['CurrentBranchChanged'] = _CURRENTBRANCHCHANGED
DESCRIPTOR.message_types_by_name['ShardOwnershipLost'] = _SHARDOWNERSHIPLOST
DESCRIPTOR.message_types_by_name['NamespaceAlreadyExists'] = _NAMESPACEALREADYEXISTS
DESCRIPTOR.message_types_by_name['CancellationAlreadyRequested'] = _CANCELLATIONALREADYREQUESTED
DESCRIPTOR.message_types_by_name['QueryFailed'] = _QUERYFAILED
DESCRIPTOR.message_types_by_name['EventAlreadyStarted'] = _EVENTALREADYSTARTED
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NotFound = _reflection.GeneratedProtocolMessageType('NotFound', (_message.Message,), {
  'DESCRIPTOR' : _NOTFOUND,
  '__module__' : 'temporal.proto.failure.message_pb2'
  # @@protoc_insertion_point(class_scope:failure.NotFound)
  })
_sym_db.RegisterMessage(NotFound)

WorkflowExecutionAlreadyStarted = _reflection.GeneratedProtocolMessageType('WorkflowExecutionAlreadyStarted', (_message.Message,), {
  'DESCRIPTOR' : _WORKFLOWEXECUTIONALREADYSTARTED,
  '__module__' : 'temporal.proto.failure.message_pb2'
  # @@protoc_insertion_point(class_scope:failure.WorkflowExecutionAlreadyStarted)
  })
_sym_db.RegisterMessage(WorkflowExecutionAlreadyStarted)

NamespaceNotActive = _reflection.GeneratedProtocolMessageType('NamespaceNotActive', (_message.Message,), {
  'DESCRIPTOR' : _NAMESPACENOTACTIVE,
  '__module__' : 'temporal.proto.failure.message_pb2'
  # @@protoc_insertion_point(class_scope:failure.NamespaceNotActive)
  })
_sym_db.RegisterMessage(NamespaceNotActive)

RetryTask = _reflection.GeneratedProtocolMessageType('RetryTask', (_message.Message,), {
  'DESCRIPTOR' : _RETRYTASK,
  '__module__' : 'temporal.proto.failure.message_pb2'
  # @@protoc_insertion_point(class_scope:failure.RetryTask)
  })
_sym_db.RegisterMessage(RetryTask)

RetryTaskV2 = _reflection.GeneratedProtocolMessageType('RetryTaskV2', (_message.Message,), {
  'DESCRIPTOR' : _RETRYTASKV2,
  '__module__' : 'temporal.proto.failure.message_pb2'
  # @@protoc_insertion_point(class_scope:failure.RetryTaskV2)
  })
_sym_db.RegisterMessage(RetryTaskV2)

ClientVersionNotSupported = _reflection.GeneratedProtocolMessageType('ClientVersionNotSupported', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTVERSIONNOTSUPPORTED,
  '__module__' : 'temporal.proto.failure.message_pb2'
  # @@protoc_insertion_point(class_scope:failure.ClientVersionNotSupported)
  })
_sym_db.RegisterMessage(ClientVersionNotSupported)

FeatureVersionNotSupported = _reflection.GeneratedProtocolMessageType('FeatureVersionNotSupported', (_message.Message,), {
  'DESCRIPTOR' : _FEATUREVERSIONNOTSUPPORTED,
  '__module__' : 'temporal.proto.failure.message_pb2'
  # @@protoc_insertion_point(class_scope:failure.FeatureVersionNotSupported)
  })
_sym_db.RegisterMessage(FeatureVersionNotSupported)

CurrentBranchChanged = _reflection.GeneratedProtocolMessageType('CurrentBranchChanged', (_message.Message,), {
  'DESCRIPTOR' : _CURRENTBRANCHCHANGED,
  '__module__' : 'temporal.proto.failure.message_pb2'
  # @@protoc_insertion_point(class_scope:failure.CurrentBranchChanged)
  })
_sym_db.RegisterMessage(CurrentBranchChanged)

ShardOwnershipLost = _reflection.GeneratedProtocolMessageType('ShardOwnershipLost', (_message.Message,), {
  'DESCRIPTOR' : _SHARDOWNERSHIPLOST,
  '__module__' : 'temporal.proto.failure.message_pb2'
  # @@protoc_insertion_point(class_scope:failure.ShardOwnershipLost)
  })
_sym_db.RegisterMessage(ShardOwnershipLost)

NamespaceAlreadyExists = _reflection.GeneratedProtocolMessageType('NamespaceAlreadyExists', (_message.Message,), {
  'DESCRIPTOR' : _NAMESPACEALREADYEXISTS,
  '__module__' : 'temporal.proto.failure.message_pb2'
  # @@protoc_insertion_point(class_scope:failure.NamespaceAlreadyExists)
  })
_sym_db.RegisterMessage(NamespaceAlreadyExists)

CancellationAlreadyRequested = _reflection.GeneratedProtocolMessageType('CancellationAlreadyRequested', (_message.Message,), {
  'DESCRIPTOR' : _CANCELLATIONALREADYREQUESTED,
  '__module__' : 'temporal.proto.failure.message_pb2'
  # @@protoc_insertion_point(class_scope:failure.CancellationAlreadyRequested)
  })
_sym_db.RegisterMessage(CancellationAlreadyRequested)

QueryFailed = _reflection.GeneratedProtocolMessageType('QueryFailed', (_message.Message,), {
  'DESCRIPTOR' : _QUERYFAILED,
  '__module__' : 'temporal.proto.failure.message_pb2'
  # @@protoc_insertion_point(class_scope:failure.QueryFailed)
  })
_sym_db.RegisterMessage(QueryFailed)

EventAlreadyStarted = _reflection.GeneratedProtocolMessageType('EventAlreadyStarted', (_message.Message,), {
  'DESCRIPTOR' : _EVENTALREADYSTARTED,
  '__module__' : 'temporal.proto.failure.message_pb2'
  # @@protoc_insertion_point(class_scope:failure.EventAlreadyStarted)
  })
_sym_db.RegisterMessage(EventAlreadyStarted)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)