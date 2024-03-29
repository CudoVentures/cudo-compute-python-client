# coding: utf-8

"""
    Cudo Compute service

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from src.cudo_compute.configuration import Configuration


class Invoice(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'amount_due': 'str',
        'amount_paid': 'str',
        'amount_remaining': 'str',
        'auto_advance': 'bool',
        'billing_reason': 'str',
        'created': 'str',
        'currency': 'str',
        'description': 'str',
        'due_date': 'str',
        'hosted_invoice_url': 'str',
        'id': 'str',
        'number': 'str',
        'paid_date': 'str',
        'period_end': 'str',
        'period_start': 'str',
        'status': 'str'
    }

    attribute_map = {
        'amount_due': 'amountDue',
        'amount_paid': 'amountPaid',
        'amount_remaining': 'amountRemaining',
        'auto_advance': 'autoAdvance',
        'billing_reason': 'billingReason',
        'created': 'created',
        'currency': 'currency',
        'description': 'description',
        'due_date': 'dueDate',
        'hosted_invoice_url': 'hostedInvoiceUrl',
        'id': 'id',
        'number': 'number',
        'paid_date': 'paidDate',
        'period_end': 'periodEnd',
        'period_start': 'periodStart',
        'status': 'status'
    }

    def __init__(self, amount_due=None, amount_paid=None, amount_remaining=None, auto_advance=None, billing_reason=None, created=None, currency=None, description=None, due_date=None, hosted_invoice_url=None, id=None, number=None, paid_date=None, period_end=None, period_start=None, status=None, _configuration=None):  # noqa: E501
        """Invoice - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._amount_due = None
        self._amount_paid = None
        self._amount_remaining = None
        self._auto_advance = None
        self._billing_reason = None
        self._created = None
        self._currency = None
        self._description = None
        self._due_date = None
        self._hosted_invoice_url = None
        self._id = None
        self._number = None
        self._paid_date = None
        self._period_end = None
        self._period_start = None
        self._status = None
        self.discriminator = None

        if amount_due is not None:
            self.amount_due = amount_due
        if amount_paid is not None:
            self.amount_paid = amount_paid
        if amount_remaining is not None:
            self.amount_remaining = amount_remaining
        if auto_advance is not None:
            self.auto_advance = auto_advance
        if billing_reason is not None:
            self.billing_reason = billing_reason
        if created is not None:
            self.created = created
        if currency is not None:
            self.currency = currency
        if description is not None:
            self.description = description
        if due_date is not None:
            self.due_date = due_date
        if hosted_invoice_url is not None:
            self.hosted_invoice_url = hosted_invoice_url
        if id is not None:
            self.id = id
        if number is not None:
            self.number = number
        if paid_date is not None:
            self.paid_date = paid_date
        if period_end is not None:
            self.period_end = period_end
        if period_start is not None:
            self.period_start = period_start
        if status is not None:
            self.status = status

    @property
    def amount_due(self):
        """Gets the amount_due of this Invoice.  # noqa: E501


        :return: The amount_due of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._amount_due

    @amount_due.setter
    def amount_due(self, amount_due):
        """Sets the amount_due of this Invoice.


        :param amount_due: The amount_due of this Invoice.  # noqa: E501
        :type: str
        """

        self._amount_due = amount_due

    @property
    def amount_paid(self):
        """Gets the amount_paid of this Invoice.  # noqa: E501


        :return: The amount_paid of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._amount_paid

    @amount_paid.setter
    def amount_paid(self, amount_paid):
        """Sets the amount_paid of this Invoice.


        :param amount_paid: The amount_paid of this Invoice.  # noqa: E501
        :type: str
        """

        self._amount_paid = amount_paid

    @property
    def amount_remaining(self):
        """Gets the amount_remaining of this Invoice.  # noqa: E501


        :return: The amount_remaining of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._amount_remaining

    @amount_remaining.setter
    def amount_remaining(self, amount_remaining):
        """Sets the amount_remaining of this Invoice.


        :param amount_remaining: The amount_remaining of this Invoice.  # noqa: E501
        :type: str
        """

        self._amount_remaining = amount_remaining

    @property
    def auto_advance(self):
        """Gets the auto_advance of this Invoice.  # noqa: E501


        :return: The auto_advance of this Invoice.  # noqa: E501
        :rtype: bool
        """
        return self._auto_advance

    @auto_advance.setter
    def auto_advance(self, auto_advance):
        """Sets the auto_advance of this Invoice.


        :param auto_advance: The auto_advance of this Invoice.  # noqa: E501
        :type: bool
        """

        self._auto_advance = auto_advance

    @property
    def billing_reason(self):
        """Gets the billing_reason of this Invoice.  # noqa: E501


        :return: The billing_reason of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._billing_reason

    @billing_reason.setter
    def billing_reason(self, billing_reason):
        """Sets the billing_reason of this Invoice.


        :param billing_reason: The billing_reason of this Invoice.  # noqa: E501
        :type: str
        """

        self._billing_reason = billing_reason

    @property
    def created(self):
        """Gets the created of this Invoice.  # noqa: E501


        :return: The created of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Invoice.


        :param created: The created of this Invoice.  # noqa: E501
        :type: str
        """

        self._created = created

    @property
    def currency(self):
        """Gets the currency of this Invoice.  # noqa: E501


        :return: The currency of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this Invoice.


        :param currency: The currency of this Invoice.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def description(self):
        """Gets the description of this Invoice.  # noqa: E501


        :return: The description of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Invoice.


        :param description: The description of this Invoice.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def due_date(self):
        """Gets the due_date of this Invoice.  # noqa: E501


        :return: The due_date of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this Invoice.


        :param due_date: The due_date of this Invoice.  # noqa: E501
        :type: str
        """

        self._due_date = due_date

    @property
    def hosted_invoice_url(self):
        """Gets the hosted_invoice_url of this Invoice.  # noqa: E501


        :return: The hosted_invoice_url of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._hosted_invoice_url

    @hosted_invoice_url.setter
    def hosted_invoice_url(self, hosted_invoice_url):
        """Sets the hosted_invoice_url of this Invoice.


        :param hosted_invoice_url: The hosted_invoice_url of this Invoice.  # noqa: E501
        :type: str
        """

        self._hosted_invoice_url = hosted_invoice_url

    @property
    def id(self):
        """Gets the id of this Invoice.  # noqa: E501


        :return: The id of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Invoice.


        :param id: The id of this Invoice.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def number(self):
        """Gets the number of this Invoice.  # noqa: E501


        :return: The number of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this Invoice.


        :param number: The number of this Invoice.  # noqa: E501
        :type: str
        """

        self._number = number

    @property
    def paid_date(self):
        """Gets the paid_date of this Invoice.  # noqa: E501


        :return: The paid_date of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._paid_date

    @paid_date.setter
    def paid_date(self, paid_date):
        """Sets the paid_date of this Invoice.


        :param paid_date: The paid_date of this Invoice.  # noqa: E501
        :type: str
        """

        self._paid_date = paid_date

    @property
    def period_end(self):
        """Gets the period_end of this Invoice.  # noqa: E501


        :return: The period_end of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._period_end

    @period_end.setter
    def period_end(self, period_end):
        """Sets the period_end of this Invoice.


        :param period_end: The period_end of this Invoice.  # noqa: E501
        :type: str
        """

        self._period_end = period_end

    @property
    def period_start(self):
        """Gets the period_start of this Invoice.  # noqa: E501


        :return: The period_start of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._period_start

    @period_start.setter
    def period_start(self, period_start):
        """Sets the period_start of this Invoice.


        :param period_start: The period_start of this Invoice.  # noqa: E501
        :type: str
        """

        self._period_start = period_start

    @property
    def status(self):
        """Gets the status of this Invoice.  # noqa: E501


        :return: The status of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Invoice.


        :param status: The status of this Invoice.  # noqa: E501
        :type: str
        """

        self._status = status

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Invoice, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Invoice):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Invoice):
            return True

        return self.to_dict() != other.to_dict()
