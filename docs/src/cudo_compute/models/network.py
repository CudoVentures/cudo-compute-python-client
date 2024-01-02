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


class Network(object):
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
        'active_state': 'str',
        'data_center_id': 'str',
        'external_ip_address': 'str',
        'gateway': 'str',
        'id': 'str',
        'init_state': 'str',
        'internal_ip_address': 'str',
        'ip_range': 'str',
        'network_state': 'NetworkState',
        'price_hr': 'Decimal',
        'short_state': 'str',
        'size': 'VRouterSize'
    }

    attribute_map = {
        'active_state': 'activeState',
        'data_center_id': 'dataCenterId',
        'external_ip_address': 'externalIpAddress',
        'gateway': 'gateway',
        'id': 'id',
        'init_state': 'initState',
        'internal_ip_address': 'internalIpAddress',
        'ip_range': 'ipRange',
        'network_state': 'networkState',
        'price_hr': 'priceHr',
        'short_state': 'shortState',
        'size': 'size'
    }

    def __init__(self, active_state=None, data_center_id=None, external_ip_address=None, gateway=None, id=None, init_state=None, internal_ip_address=None, ip_range=None, network_state=None, price_hr=None, short_state=None, size=None, _configuration=None):  # noqa: E501
        """Network - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._active_state = None
        self._data_center_id = None
        self._external_ip_address = None
        self._gateway = None
        self._id = None
        self._init_state = None
        self._internal_ip_address = None
        self._ip_range = None
        self._network_state = None
        self._price_hr = None
        self._short_state = None
        self._size = None
        self.discriminator = None

        if active_state is not None:
            self.active_state = active_state
        if data_center_id is not None:
            self.data_center_id = data_center_id
        if external_ip_address is not None:
            self.external_ip_address = external_ip_address
        if gateway is not None:
            self.gateway = gateway
        if id is not None:
            self.id = id
        if init_state is not None:
            self.init_state = init_state
        if internal_ip_address is not None:
            self.internal_ip_address = internal_ip_address
        if ip_range is not None:
            self.ip_range = ip_range
        if network_state is not None:
            self.network_state = network_state
        if price_hr is not None:
            self.price_hr = price_hr
        if short_state is not None:
            self.short_state = short_state
        if size is not None:
            self.size = size

    @property
    def active_state(self):
        """Gets the active_state of this Network.  # noqa: E501


        :return: The active_state of this Network.  # noqa: E501
        :rtype: str
        """
        return self._active_state

    @active_state.setter
    def active_state(self, active_state):
        """Sets the active_state of this Network.


        :param active_state: The active_state of this Network.  # noqa: E501
        :type: str
        """

        self._active_state = active_state

    @property
    def data_center_id(self):
        """Gets the data_center_id of this Network.  # noqa: E501


        :return: The data_center_id of this Network.  # noqa: E501
        :rtype: str
        """
        return self._data_center_id

    @data_center_id.setter
    def data_center_id(self, data_center_id):
        """Sets the data_center_id of this Network.


        :param data_center_id: The data_center_id of this Network.  # noqa: E501
        :type: str
        """

        self._data_center_id = data_center_id

    @property
    def external_ip_address(self):
        """Gets the external_ip_address of this Network.  # noqa: E501


        :return: The external_ip_address of this Network.  # noqa: E501
        :rtype: str
        """
        return self._external_ip_address

    @external_ip_address.setter
    def external_ip_address(self, external_ip_address):
        """Sets the external_ip_address of this Network.


        :param external_ip_address: The external_ip_address of this Network.  # noqa: E501
        :type: str
        """

        self._external_ip_address = external_ip_address

    @property
    def gateway(self):
        """Gets the gateway of this Network.  # noqa: E501


        :return: The gateway of this Network.  # noqa: E501
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """Sets the gateway of this Network.


        :param gateway: The gateway of this Network.  # noqa: E501
        :type: str
        """

        self._gateway = gateway

    @property
    def id(self):
        """Gets the id of this Network.  # noqa: E501


        :return: The id of this Network.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Network.


        :param id: The id of this Network.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def init_state(self):
        """Gets the init_state of this Network.  # noqa: E501


        :return: The init_state of this Network.  # noqa: E501
        :rtype: str
        """
        return self._init_state

    @init_state.setter
    def init_state(self, init_state):
        """Sets the init_state of this Network.


        :param init_state: The init_state of this Network.  # noqa: E501
        :type: str
        """

        self._init_state = init_state

    @property
    def internal_ip_address(self):
        """Gets the internal_ip_address of this Network.  # noqa: E501


        :return: The internal_ip_address of this Network.  # noqa: E501
        :rtype: str
        """
        return self._internal_ip_address

    @internal_ip_address.setter
    def internal_ip_address(self, internal_ip_address):
        """Sets the internal_ip_address of this Network.


        :param internal_ip_address: The internal_ip_address of this Network.  # noqa: E501
        :type: str
        """

        self._internal_ip_address = internal_ip_address

    @property
    def ip_range(self):
        """Gets the ip_range of this Network.  # noqa: E501


        :return: The ip_range of this Network.  # noqa: E501
        :rtype: str
        """
        return self._ip_range

    @ip_range.setter
    def ip_range(self, ip_range):
        """Sets the ip_range of this Network.


        :param ip_range: The ip_range of this Network.  # noqa: E501
        :type: str
        """

        self._ip_range = ip_range

    @property
    def network_state(self):
        """Gets the network_state of this Network.  # noqa: E501


        :return: The network_state of this Network.  # noqa: E501
        :rtype: NetworkState
        """
        return self._network_state

    @network_state.setter
    def network_state(self, network_state):
        """Sets the network_state of this Network.


        :param network_state: The network_state of this Network.  # noqa: E501
        :type: NetworkState
        """

        self._network_state = network_state

    @property
    def price_hr(self):
        """Gets the price_hr of this Network.  # noqa: E501


        :return: The price_hr of this Network.  # noqa: E501
        :rtype: Decimal
        """
        return self._price_hr

    @price_hr.setter
    def price_hr(self, price_hr):
        """Sets the price_hr of this Network.


        :param price_hr: The price_hr of this Network.  # noqa: E501
        :type: Decimal
        """

        self._price_hr = price_hr

    @property
    def short_state(self):
        """Gets the short_state of this Network.  # noqa: E501


        :return: The short_state of this Network.  # noqa: E501
        :rtype: str
        """
        return self._short_state

    @short_state.setter
    def short_state(self, short_state):
        """Sets the short_state of this Network.


        :param short_state: The short_state of this Network.  # noqa: E501
        :type: str
        """

        self._short_state = short_state

    @property
    def size(self):
        """Gets the size of this Network.  # noqa: E501


        :return: The size of this Network.  # noqa: E501
        :rtype: VRouterSize
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this Network.


        :param size: The size of this Network.  # noqa: E501
        :type: VRouterSize
        """

        self._size = size

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
        if issubclass(Network, dict):
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
        if not isinstance(other, Network):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Network):
            return True

        return self.to_dict() != other.to_dict()
