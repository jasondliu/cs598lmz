import weakref

import pytest
import yaml

from leapp import reporting
from leapp import reporting_utils


def test_actor_outcome(outcome):
    actor = 'test.actor'
    reporting.create_report([
        reporting.Title('Title'),
        reporting.Summary('Summary'),
        reporting.Severity(reporting.Severity.MEDIUM),
        reporting.Tags([reporting.Tags.NETWORK]),
        reporting.Flags([reporting.Flags.INHIBITOR]),
        reporting.Remediation(hint='Do something'),
        reporting.ExternalLink(title='Ref', url='http://ref.com'),
        reporting.RelatedResource('Resource', 'filename'),
        reporting.Details(
            reporting.Proposed("Proposed details"),
            reporting.Action("Action details")
        ),
        reporting.ReportLink('Another', 'another.source'),
        reporting.RelatedBug(12345),
        outcome(actor)])


def test_model_outcome(outcome):
    model = reporting.Model()
    reporting.create_report([
        reporting.Title
