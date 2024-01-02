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


class SecurityGroup1(object):
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
        'data_center_id': 'str',
        'description': 'str',
        'rules': 'list[Rule]'
    }

    attribute_map = {
        'data_center_id': 'dataCenterId',
        'description': 'description',
        'rules': 'rules'
    }

    def __init__(self, data_center_id=None, description=None, rules=None, _configuration=None):  # noqa: E501
        """SecurityGroup1 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._data_center_id = None
        self._description = None
        self._rules = None
        self.discriminator = None

        self.data_center_id = data_center_id
        if description is not None:
            self.description = description
        if rules is not None:
            self.rules = rules

    @property
    def data_center_id(self):
        """Gets the data_center_id of this SecurityGroup1.  # noqa: E501


        :return: The data_center_id of this SecurityGroup1.  # noqa: E501
        :rtype: str
        """
        return self._data_center_id

    @data_center_id.setter
    def data_center_id(self, data_center_id):
        """Sets the data_center_id of this SecurityGroup1.


        :param data_center_id: The data_center_id of this SecurityGroup1.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and data_center_id is None:
            raise ValueError("Invalid value for `data_center_id`, must not be `None`")  # noqa: E501

        self._data_center_id = data_center_id

    @property
    def description(self):
        """Gets the description of this SecurityGroup1.  # noqa: E501


        :return: The description of this SecurityGroup1.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SecurityGroup1.


        :param description: The description of this SecurityGroup1.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def rules(self):
        """Gets the rules of this SecurityGroup1.  # noqa: E501


        :return: The rules of this SecurityGroup1.  # noqa: E501
        :rtype: list[Rule]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this SecurityGroup1.


        :param rules: The rules of this SecurityGroup1.  # noqa: E501
        :type: list[Rule]
        """

        self._rules = rules

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
        if issubclass(SecurityGroup1, dict):
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
        if not isinstance(other, SecurityGroup1):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SecurityGroup1):
            return True

        return self.to_dict() != other.to_dict()
