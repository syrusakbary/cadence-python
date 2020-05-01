# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: temporal/proto/decision/enum.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='temporal/proto/decision/enum.proto',
  package='decision',
  syntax='proto3',
  serialized_options=b'\n\032io.temporal.proto.decisionP\001Z&go.temporal.io/temporal-proto/decision',
  serialized_pb=b'\n\"temporal/proto/decision/enum.proto\x12\x08\x64\x65\x63ision*\x8b\x03\n\x0c\x44\x65\x63isionType\x12\x18\n\x14ScheduleActivityTask\x10\x00\x12\x1d\n\x19RequestCancelActivityTask\x10\x01\x12\x0e\n\nStartTimer\x10\x02\x12\x1d\n\x19\x43ompleteWorkflowExecution\x10\x03\x12\x19\n\x15\x46\x61ilWorkflowExecution\x10\x04\x12\x0f\n\x0b\x43\x61ncelTimer\x10\x05\x12\x1b\n\x17\x43\x61ncelWorkflowExecution\x10\x06\x12*\n&RequestCancelExternalWorkflowExecution\x10\x07\x12\x10\n\x0cRecordMarker\x10\x08\x12\"\n\x1e\x43ontinueAsNewWorkflowExecution\x10\t\x12\x1f\n\x1bStartChildWorkflowExecution\x10\n\x12#\n\x1fSignalExternalWorkflowExecution\x10\x0b\x12\"\n\x1eUpsertWorkflowSearchAttributes\x10\x0c\x42\x46\n\x1aio.temporal.proto.decisionP\x01Z&go.temporal.io/temporal-proto/decisionb\x06proto3'
)

_DECISIONTYPE = _descriptor.EnumDescriptor(
  name='DecisionType',
  full_name='decision.DecisionType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ScheduleActivityTask', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RequestCancelActivityTask', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='StartTimer', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CompleteWorkflowExecution', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FailWorkflowExecution', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CancelTimer', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CancelWorkflowExecution', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RequestCancelExternalWorkflowExecution', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RecordMarker', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ContinueAsNewWorkflowExecution', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='StartChildWorkflowExecution', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SignalExternalWorkflowExecution', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UpsertWorkflowSearchAttributes', index=12, number=12,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=49,
  serialized_end=444,
)
_sym_db.RegisterEnumDescriptor(_DECISIONTYPE)

DecisionType = enum_type_wrapper.EnumTypeWrapper(_DECISIONTYPE)
ScheduleActivityTask = 0
RequestCancelActivityTask = 1
StartTimer = 2
CompleteWorkflowExecution = 3
FailWorkflowExecution = 4
CancelTimer = 5
CancelWorkflowExecution = 6
RequestCancelExternalWorkflowExecution = 7
RecordMarker = 8
ContinueAsNewWorkflowExecution = 9
StartChildWorkflowExecution = 10
SignalExternalWorkflowExecution = 11
UpsertWorkflowSearchAttributes = 12


DESCRIPTOR.enum_types_by_name['DecisionType'] = _DECISIONTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)