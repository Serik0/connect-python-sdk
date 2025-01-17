# -*- coding: utf-8 -*-

# This file is part of the Ingram Micro Cloud Blue Connect SDK.
# Copyright (c) 2019 Ingram Micro. All Rights Reserved.

from .base import BaseModel
from .company import Company
from .hub import Hub
from .product import Product
from connect.models.schemas import ConnectionSchema


class Connection(BaseModel):
    """ Represents a communication channel which provides the ability
    to order products within particular hub.

    Standalone connection is required for each product and for each provider account.
    """

    _schema = ConnectionSchema()

    type = None  # type: str
    """ (str) Type of connection. """

    provider = None  # type: Company
    """ (:py:class:`.Company`) Provider Account Reference. """

    vendor = None  # type: Company
    """ (:py:class:`.Company`) Vendor Account Reference. """

    product = None  # type: Product
    """ (:py:class:`.Product`) Product Reference. """

    hub = None  # type: Hub
    """ (:py:class:`.Hub`) Hub Reference. """
