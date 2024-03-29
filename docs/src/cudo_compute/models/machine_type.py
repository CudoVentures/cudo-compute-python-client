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


class MachineType(object):
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
        'count_clusters': 'int',
        'count_hosts': 'int',
        'count_hosts_active': 'int',
        'count_hosts_inactive': 'int',
        'machine_type': 'str'
    }

    attribute_map = {
        'count_clusters': 'countClusters',
        'count_hosts': 'countHosts',
        'count_hosts_active': 'countHostsActive',
        'count_hosts_inactive': 'countHostsInactive',
        'machine_type': 'machineType'
    }

    def __init__(self, count_clusters=None, count_hosts=None, count_hosts_active=None, count_hosts_inactive=None, machine_type=None, _configuration=None):  # noqa: E501
        """MachineType - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._count_clusters = None
        self._count_hosts = None
        self._count_hosts_active = None
        self._count_hosts_inactive = None
        self._machine_type = None
        self.discriminator = None

        self.count_clusters = count_clusters
        self.count_hosts = count_hosts
        self.count_hosts_active = count_hosts_active
        self.count_hosts_inactive = count_hosts_inactive
        self.machine_type = machine_type

    @property
    def count_clusters(self):
        """Gets the count_clusters of this MachineType.  # noqa: E501


        :return: The count_clusters of this MachineType.  # noqa: E501
        :rtype: int
        """
        return self._count_clusters

    @count_clusters.setter
    def count_clusters(self, count_clusters):
        """Sets the count_clusters of this MachineType.


        :param count_clusters: The count_clusters of this MachineType.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and count_clusters is None:
            raise ValueError("Invalid value for `count_clusters`, must not be `None`")  # noqa: E501

        self._count_clusters = count_clusters

    @property
    def count_hosts(self):
        """Gets the count_hosts of this MachineType.  # noqa: E501


        :return: The count_hosts of this MachineType.  # noqa: E501
        :rtype: int
        """
        return self._count_hosts

    @count_hosts.setter
    def count_hosts(self, count_hosts):
        """Sets the count_hosts of this MachineType.


        :param count_hosts: The count_hosts of this MachineType.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and count_hosts is None:
            raise ValueError("Invalid value for `count_hosts`, must not be `None`")  # noqa: E501

        self._count_hosts = count_hosts

    @property
    def count_hosts_active(self):
        """Gets the count_hosts_active of this MachineType.  # noqa: E501


        :return: The count_hosts_active of this MachineType.  # noqa: E501
        :rtype: int
        """
        return self._count_hosts_active

    @count_hosts_active.setter
    def count_hosts_active(self, count_hosts_active):
        """Sets the count_hosts_active of this MachineType.


        :param count_hosts_active: The count_hosts_active of this MachineType.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and count_hosts_active is None:
            raise ValueError("Invalid value for `count_hosts_active`, must not be `None`")  # noqa: E501

        self._count_hosts_active = count_hosts_active

    @property
    def count_hosts_inactive(self):
        """Gets the count_hosts_inactive of this MachineType.  # noqa: E501


        :return: The count_hosts_inactive of this MachineType.  # noqa: E501
        :rtype: int
        """
        return self._count_hosts_inactive

    @count_hosts_inactive.setter
    def count_hosts_inactive(self, count_hosts_inactive):
        """Sets the count_hosts_inactive of this MachineType.


        :param count_hosts_inactive: The count_hosts_inactive of this MachineType.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and count_hosts_inactive is None:
            raise ValueError("Invalid value for `count_hosts_inactive`, must not be `None`")  # noqa: E501

        self._count_hosts_inactive = count_hosts_inactive

    @property
    def machine_type(self):
        """Gets the machine_type of this MachineType.  # noqa: E501


        :return: The machine_type of this MachineType.  # noqa: E501
        :rtype: str
        """
        return self._machine_type

    @machine_type.setter
    def machine_type(self, machine_type):
        """Sets the machine_type of this MachineType.


        :param machine_type: The machine_type of this MachineType.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and machine_type is None:
            raise ValueError("Invalid value for `machine_type`, must not be `None`")  # noqa: E501

        self._machine_type = machine_type

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
        if issubclass(MachineType, dict):
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
        if not isinstance(other, MachineType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MachineType):
            return True

        return self.to_dict() != other.to_dict()
