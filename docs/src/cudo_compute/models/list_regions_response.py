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


class ListRegionsResponse(object):
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
        'regions': 'list[Region]'
    }

    attribute_map = {
        'regions': 'regions'
    }

    def __init__(self, regions=None, _configuration=None):  # noqa: E501
        """ListRegionsResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._regions = None
        self.discriminator = None

        self.regions = regions

    @property
    def regions(self):
        """Gets the regions of this ListRegionsResponse.  # noqa: E501


        :return: The regions of this ListRegionsResponse.  # noqa: E501
        :rtype: list[Region]
        """
        return self._regions

    @regions.setter
    def regions(self, regions):
        """Sets the regions of this ListRegionsResponse.


        :param regions: The regions of this ListRegionsResponse.  # noqa: E501
        :type: list[Region]
        """
        if self._configuration.client_side_validation and regions is None:
            raise ValueError("Invalid value for `regions`, must not be `None`")  # noqa: E501

        self._regions = regions

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
        if issubclass(ListRegionsResponse, dict):
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
        if not isinstance(other, ListRegionsResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListRegionsResponse):
            return True

        return self.to_dict() != other.to_dict()
