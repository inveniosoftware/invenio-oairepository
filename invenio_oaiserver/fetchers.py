# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2016-2018 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Persistent identifier fetchers."""

from __future__ import absolute_import, print_function
from invenio_oaiserver.provider import OAIIDProvider

from invenio_pidstore.errors import PersistentIdentifierError
from invenio_pidstore.fetchers import FetchedPID
from invenio_rdm_records.proxies import current_rdm_records


def oaiid_fetcher(data):
    """Fetch a record's identifier.

    :param data: The record data.
    :returns: A :class:`invenio_pidstore.fetchers.FetchedPID` instance.
    """
    pid_value = data.get('pids', {}).get('oai', {}).get('identifier')

    if not pid_value:
        raise PersistentIdentifierError

    return FetchedPID(
        provider=OAIIDProvider,
        pid_type="oai",
        pid_value=str(pid_value),
    )

def oai_record_sets_fetcher(record):
    """Fetch a record's sets."""
    return record.get('_oai', {}).get('sets', [])
