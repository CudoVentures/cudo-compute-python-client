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


class UserPermission(object):
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
        'permission_role': 'Role',
        'role': 'str',
        'user_email': 'str',
        'user_id': 'str',
        'user_picture': 'str'
    }

    attribute_map = {
        'permission_role': 'permissionRole',
        'role': 'role',
        'user_email': 'userEmail',
        'user_id': 'userId',
        'user_picture': 'userPicture'
    }

    def __init__(self, permission_role=None, role=None, user_email=None, user_id=None, user_picture=None, _configuration=None):  # noqa: E501
        """UserPermission - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._permission_role = None
        self._role = None
        self._user_email = None
        self._user_id = None
        self._user_picture = None
        self.discriminator = None

        self.permission_role = permission_role
        self.role = role
        self.user_email = user_email
        self.user_id = user_id
        self.user_picture = user_picture

    @property
    def permission_role(self):
        """Gets the permission_role of this UserPermission.  # noqa: E501


        :return: The permission_role of this UserPermission.  # noqa: E501
        :rtype: Role
        """
        return self._permission_role

    @permission_role.setter
    def permission_role(self, permission_role):
        """Sets the permission_role of this UserPermission.


        :param permission_role: The permission_role of this UserPermission.  # noqa: E501
        :type: Role
        """
        if self._configuration.client_side_validation and permission_role is None:
            raise ValueError("Invalid value for `permission_role`, must not be `None`")  # noqa: E501

        self._permission_role = permission_role

    @property
    def role(self):
        """Gets the role of this UserPermission.  # noqa: E501


        :return: The role of this UserPermission.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this UserPermission.


        :param role: The role of this UserPermission.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and role is None:
            raise ValueError("Invalid value for `role`, must not be `None`")  # noqa: E501

        self._role = role

    @property
    def user_email(self):
        """Gets the user_email of this UserPermission.  # noqa: E501


        :return: The user_email of this UserPermission.  # noqa: E501
        :rtype: str
        """
        return self._user_email

    @user_email.setter
    def user_email(self, user_email):
        """Sets the user_email of this UserPermission.


        :param user_email: The user_email of this UserPermission.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and user_email is None:
            raise ValueError("Invalid value for `user_email`, must not be `None`")  # noqa: E501

        self._user_email = user_email

    @property
    def user_id(self):
        """Gets the user_id of this UserPermission.  # noqa: E501


        :return: The user_id of this UserPermission.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this UserPermission.


        :param user_id: The user_id of this UserPermission.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def user_picture(self):
        """Gets the user_picture of this UserPermission.  # noqa: E501


        :return: The user_picture of this UserPermission.  # noqa: E501
        :rtype: str
        """
        return self._user_picture

    @user_picture.setter
    def user_picture(self, user_picture):
        """Sets the user_picture of this UserPermission.


        :param user_picture: The user_picture of this UserPermission.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and user_picture is None:
            raise ValueError("Invalid value for `user_picture`, must not be `None`")  # noqa: E501

        self._user_picture = user_picture

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
        if issubclass(UserPermission, dict):
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
        if not isinstance(other, UserPermission):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserPermission):
            return True

        return self.to_dict() != other.to_dict()