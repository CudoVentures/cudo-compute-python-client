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


class GetMachineTypeLiveUtilizationResponse(object):
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
        'cpu_utilization': 'float',
        'gpu_free': 'int',
        'gpu_total': 'int',
        'gpu_used': 'int',
        'gpu_utilization': 'float',
        'memory_gib_free': 'int',
        'memory_gib_total': 'int',
        'memory_gib_used': 'int',
        'memory_utilization': 'float',
        'utilization': 'float',
        'vcpu_free': 'int',
        'vcpu_total': 'int',
        'vcpu_used': 'int'
    }

    attribute_map = {
        'cpu_utilization': 'cpuUtilization',
        'gpu_free': 'gpuFree',
        'gpu_total': 'gpuTotal',
        'gpu_used': 'gpuUsed',
        'gpu_utilization': 'gpuUtilization',
        'memory_gib_free': 'memoryGibFree',
        'memory_gib_total': 'memoryGibTotal',
        'memory_gib_used': 'memoryGibUsed',
        'memory_utilization': 'memoryUtilization',
        'utilization': 'utilization',
        'vcpu_free': 'vcpuFree',
        'vcpu_total': 'vcpuTotal',
        'vcpu_used': 'vcpuUsed'
    }

    def __init__(self, cpu_utilization=None, gpu_free=None, gpu_total=None, gpu_used=None, gpu_utilization=None, memory_gib_free=None, memory_gib_total=None, memory_gib_used=None, memory_utilization=None, utilization=None, vcpu_free=None, vcpu_total=None, vcpu_used=None, _configuration=None):  # noqa: E501
        """GetMachineTypeLiveUtilizationResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cpu_utilization = None
        self._gpu_free = None
        self._gpu_total = None
        self._gpu_used = None
        self._gpu_utilization = None
        self._memory_gib_free = None
        self._memory_gib_total = None
        self._memory_gib_used = None
        self._memory_utilization = None
        self._utilization = None
        self._vcpu_free = None
        self._vcpu_total = None
        self._vcpu_used = None
        self.discriminator = None

        self.cpu_utilization = cpu_utilization
        self.gpu_free = gpu_free
        self.gpu_total = gpu_total
        self.gpu_used = gpu_used
        self.gpu_utilization = gpu_utilization
        self.memory_gib_free = memory_gib_free
        self.memory_gib_total = memory_gib_total
        self.memory_gib_used = memory_gib_used
        self.memory_utilization = memory_utilization
        self.utilization = utilization
        self.vcpu_free = vcpu_free
        self.vcpu_total = vcpu_total
        self.vcpu_used = vcpu_used

    @property
    def cpu_utilization(self):
        """Gets the cpu_utilization of this GetMachineTypeLiveUtilizationResponse.  # noqa: E501


        :return: The cpu_utilization of this GetMachineTypeLiveUtilizationResponse.  # noqa: E501
        :rtype: float
        """
        return self._cpu_utilization

    @cpu_utilization.setter
    def cpu_utilization(self, cpu_utilization):
        """Sets the cpu_utilization of this GetMachineTypeLiveUtilizationResponse.


        :param cpu_utilization: The cpu_utilization of this GetMachineTypeLiveUtilizationResponse.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and cpu_utilization is None:
            raise ValueError("Invalid value for `cpu_utilization`, must not be `None`")  # noqa: E501

        self._cpu_utilization = cpu_utilization

    @property
    def gpu_free(self):
        """Gets the gpu_free of this GetMachineTypeLiveUtilizationResponse.  # noqa: E501


        :return: The gpu_free of this GetMachineTypeLiveUtilizationResponse.  # noqa: E501
        :rtype: int
        """
        return self._gpu_free

    @gpu_free.setter
    def gpu_free(self, gpu_free):
        """Sets the gpu_free of this GetMachineTypeLiveUtilizationResponse.


        :param gpu_free: The gpu_free of this GetMachineTypeLiveUtilizationResponse.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and gpu_free is None:
            raise ValueError("Invalid value for `gpu_free`, must not be `None`")  # noqa: E501

        self._gpu_free = gpu_free

    @property
    def gpu_total(self):
        """Gets the gpu_total of this GetMachineTypeLiveUtilizationResponse.  # noqa: E501


        :return: The gpu_total of this GetMachineTypeLiveUtilizationResponse.  # noqa: E501
        :rtype: int
        """
        return self._gpu_total

    @gpu_total.setter
    def gpu_total(self, gpu_total):
        """Sets the gpu_total of this GetMachineTypeLiveUtilizationResponse.


        :param gpu_total: The gpu_total of this GetMachineTypeLiveUtilizationResponse.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and gpu_total is None:
            raise ValueError("Invalid value for `gpu_total`, must not be `None`")  # noqa: E501

        self._gpu_total = gpu_total

    @property
    def gpu_used(self):
        """Gets the gpu_used of this GetMachineTypeLiveUtilizationResponse.  # noqa: E501


        :return: The gpu_used of this GetMachineTypeLiveUtilizationResponse.  # noqa: E501
        :rtype: int
        """
        return self._gpu_used

    @gpu_used.setter
    def gpu_used(self, gpu_used):
        """Sets the gpu_used of this GetMachineTypeLiveUtilizationResponse.


        :param gpu_used: The gpu_used of this GetMachineTypeLiveUtilizationResponse.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and gpu_used is None:
            raise ValueError("Invalid value for `gpu_used`, must not be `None`")  # noqa: E501

        self._gpu_used = gpu_used

    @property
    def gpu_utilization(self):
        """Gets the gpu_utilization of this GetMachineTypeLiveUtilizationResponse.  # noqa: E501


        :return: The gpu_utilization of this GetMachineTypeLiveUtilizationResponse.  # noqa: E501
        :rtype: float
        """
        return self._gpu_utilization

    @gpu_utilization.setter
    def gpu_utilization(self, gpu_utilization):
        """Sets the gpu_utilization of this GetMachineTypeLiveUtilizationResponse.


        :param gpu_utilization: The gpu_utilization of this GetMachineTypeLiveUtilizationResponse.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and gpu_utilization is None:
            raise ValueError("Invalid value for `gpu_utilization`, must not be `None`")  # noqa: E501

        self._gpu_utilization = gpu_utilization

    @property
    def memory_gib_free(self):
        """Gets the memory_gib_free of this GetMachineTypeLiveUtilizationResponse.  # noqa: E501


        :return: The memory_gib_free of this GetMachineTypeLiveUtilizationResponse.  # noqa: E501
        :rtype: int
        """
        return self._memory_gib_free

    @memory_gib_free.setter
    def memory_gib_free(self, memory_gib_free):
        """Sets the memory_gib_free of this GetMachineTypeLiveUtilizationResponse.


        :param memory_gib_free: The memory_gib_free of this GetMachineTypeLiveUtilizationResponse.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and memory_gib_free is None:
            raise ValueError("Invalid value for `memory_gib_free`, must not be `None`")  # noqa: E501

        self._memory_gib_free = memory_gib_free

    @property
    def memory_gib_total(self):
        """Gets the memory_gib_total of this GetMachineTypeLiveUtilizationResponse.  # noqa: E501


        :return: The memory_gib_total of this GetMachineTypeLiveUtilizationResponse.  # noqa: E501
        :rtype: int
        """
        return self._memory_gib_total

    @memory_gib_total.setter
    def memory_gib_total(self, memory_gib_total):
        """Sets the memory_gib_total of this GetMachineTypeLiveUtilizationResponse.


        :param memory_gib_total: The memory_gib_total of this GetMachineTypeLiveUtilizationResponse.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and memory_gib_total is None:
            raise ValueError("Invalid value for `memory_gib_total`, must not be `None`")  # noqa: E501

        self._memory_gib_total = memory_gib_total

    @property
    def memory_gib_used(self):
        """Gets the memory_gib_used of this GetMachineTypeLiveUtilizationResponse.  # noqa: E501


        :return: The memory_gib_used of this GetMachineTypeLiveUtilizationResponse.  # noqa: E501
        :rtype: int
        """
        return self._memory_gib_used

    @memory_gib_used.setter
    def memory_gib_used(self, memory_gib_used):
        """Sets the memory_gib_used of this GetMachineTypeLiveUtilizationResponse.


        :param memory_gib_used: The memory_gib_used of this GetMachineTypeLiveUtilizationResponse.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and memory_gib_used is None:
            raise ValueError("Invalid value for `memory_gib_used`, must not be `None`")  # noqa: E501

        self._memory_gib_used = memory_gib_used

    @property
    def memory_utilization(self):
        """Gets the memory_utilization of this GetMachineTypeLiveUtilizationResponse.  # noqa: E501


        :return: The memory_utilization of this GetMachineTypeLiveUtilizationResponse.  # noqa: E501
        :rtype: float
        """
        return self._memory_utilization

    @memory_utilization.setter
    def memory_utilization(self, memory_utilization):
        """Sets the memory_utilization of this GetMachineTypeLiveUtilizationResponse.


        :param memory_utilization: The memory_utilization of this GetMachineTypeLiveUtilizationResponse.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and memory_utilization is None:
            raise ValueError("Invalid value for `memory_utilization`, must not be `None`")  # noqa: E501

        self._memory_utilization = memory_utilization

    @property
    def utilization(self):
        """Gets the utilization of this GetMachineTypeLiveUtilizationResponse.  # noqa: E501


        :return: The utilization of this GetMachineTypeLiveUtilizationResponse.  # noqa: E501
        :rtype: float
        """
        return self._utilization

    @utilization.setter
    def utilization(self, utilization):
        """Sets the utilization of this GetMachineTypeLiveUtilizationResponse.


        :param utilization: The utilization of this GetMachineTypeLiveUtilizationResponse.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and utilization is None:
            raise ValueError("Invalid value for `utilization`, must not be `None`")  # noqa: E501

        self._utilization = utilization

    @property
    def vcpu_free(self):
        """Gets the vcpu_free of this GetMachineTypeLiveUtilizationResponse.  # noqa: E501


        :return: The vcpu_free of this GetMachineTypeLiveUtilizationResponse.  # noqa: E501
        :rtype: int
        """
        return self._vcpu_free

    @vcpu_free.setter
    def vcpu_free(self, vcpu_free):
        """Sets the vcpu_free of this GetMachineTypeLiveUtilizationResponse.


        :param vcpu_free: The vcpu_free of this GetMachineTypeLiveUtilizationResponse.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and vcpu_free is None:
            raise ValueError("Invalid value for `vcpu_free`, must not be `None`")  # noqa: E501

        self._vcpu_free = vcpu_free

    @property
    def vcpu_total(self):
        """Gets the vcpu_total of this GetMachineTypeLiveUtilizationResponse.  # noqa: E501


        :return: The vcpu_total of this GetMachineTypeLiveUtilizationResponse.  # noqa: E501
        :rtype: int
        """
        return self._vcpu_total

    @vcpu_total.setter
    def vcpu_total(self, vcpu_total):
        """Sets the vcpu_total of this GetMachineTypeLiveUtilizationResponse.


        :param vcpu_total: The vcpu_total of this GetMachineTypeLiveUtilizationResponse.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and vcpu_total is None:
            raise ValueError("Invalid value for `vcpu_total`, must not be `None`")  # noqa: E501

        self._vcpu_total = vcpu_total

    @property
    def vcpu_used(self):
        """Gets the vcpu_used of this GetMachineTypeLiveUtilizationResponse.  # noqa: E501


        :return: The vcpu_used of this GetMachineTypeLiveUtilizationResponse.  # noqa: E501
        :rtype: int
        """
        return self._vcpu_used

    @vcpu_used.setter
    def vcpu_used(self, vcpu_used):
        """Sets the vcpu_used of this GetMachineTypeLiveUtilizationResponse.


        :param vcpu_used: The vcpu_used of this GetMachineTypeLiveUtilizationResponse.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and vcpu_used is None:
            raise ValueError("Invalid value for `vcpu_used`, must not be `None`")  # noqa: E501

        self._vcpu_used = vcpu_used

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
        if issubclass(GetMachineTypeLiveUtilizationResponse, dict):
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
        if not isinstance(other, GetMachineTypeLiveUtilizationResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetMachineTypeLiveUtilizationResponse):
            return True

        return self.to_dict() != other.to_dict()
