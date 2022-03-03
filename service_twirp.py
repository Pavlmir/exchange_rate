# -*- coding: utf-8 -*-
# Generated by https://github.com/verloop/twirpy/protoc-gen-twirpy.  DO NOT EDIT!
# source: service.proto

from google.protobuf import symbol_database as _symbol_database

from twirp.base import Endpoint
from twirp.server import TwirpServer
from twirp.client import TwirpClient

_sym_db = _symbol_database.Default()

class DollarRateServer(TwirpServer):

	def __init__(self, *args, service, server_path_prefix="/twirp"):
		super().__init__(service=service)
		self._prefix = F"{server_path_prefix}/twirp.example.haberdasher.DollarRate"
		self._endpoints = {
			"GetDollarRate": Endpoint(
				service_name="DollarRate",
				name="GetDollarRate",
				function=getattr(service, "GetDollarRate"),
				input=_sym_db.GetSymbol("twirp.example.haberdasher.Empty"),
				output=_sym_db.GetSymbol("twirp.example.haberdasher.Dollar"),
			),
		}

class DollarRateClient(TwirpClient):

	def GetDollarRate(self, *args, ctx, request, server_path_prefix="/twirp", **kwargs):
		return self._make_request(
			url=F"{server_path_prefix}/twirp.example.haberdasher.DollarRate/GetDollarRate",
			ctx=ctx,
			request=request,
			response_obj=_sym_db.GetSymbol("twirp.example.haberdasher.Dollar"),
			**kwargs,
		)