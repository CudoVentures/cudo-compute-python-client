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


class VM(object):
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
        'boot_disk': 'Disk',
        'boot_disk_size_gib': 'int',
        'cpu_model': 'str',
        'create_by': 'str',
        'datacenter_id': 'str',
        'external_ip_address': 'str',
        'gpu_model': 'str',
        'gpu_quantity': 'int',
        'id': 'str',
        'image_id': 'str',
        'image_name': 'str',
        'init_state': 'str',
        'internal_ip_address': 'str',
        'lcm_state': 'str',
        'machine_type': 'str',
        'memory': 'int',
        'metadata': 'dict(str, str)',
        'nics': 'list[VMNIC]',
        'one_state': 'str',
        'price_hr': 'float',
        'private_image_id': 'str',
        'public_image_id': 'str',
        'public_image_name': 'str',
        'public_ip_address': 'str',
        'region_id': 'str',
        'region_name': 'str',
        'renewable_energy': 'bool',
        'rules': 'list[SecurityGroupRule]',
        'security_group_ids': 'list[str]',
        'short_state': 'str',
        'storage_disks': 'list[Disk]',
        'vcpus': 'int',
        'vm_state': 'VmState'
    }

    attribute_map = {
        'active_state': 'activeState',
        'boot_disk': 'bootDisk',
        'boot_disk_size_gib': 'bootDiskSizeGib',
        'cpu_model': 'cpuModel',
        'create_by': 'createBy',
        'datacenter_id': 'datacenterId',
        'external_ip_address': 'externalIpAddress',
        'gpu_model': 'gpuModel',
        'gpu_quantity': 'gpuQuantity',
        'id': 'id',
        'image_id': 'imageId',
        'image_name': 'imageName',
        'init_state': 'initState',
        'internal_ip_address': 'internalIpAddress',
        'lcm_state': 'lcmState',
        'machine_type': 'machineType',
        'memory': 'memory',
        'metadata': 'metadata',
        'nics': 'nics',
        'one_state': 'oneState',
        'price_hr': 'priceHr',
        'private_image_id': 'privateImageId',
        'public_image_id': 'publicImageId',
        'public_image_name': 'publicImageName',
        'public_ip_address': 'publicIpAddress',
        'region_id': 'regionId',
        'region_name': 'regionName',
        'renewable_energy': 'renewableEnergy',
        'rules': 'rules',
        'security_group_ids': 'securityGroupIds',
        'short_state': 'shortState',
        'storage_disks': 'storageDisks',
        'vcpus': 'vcpus',
        'vm_state': 'vmState'
    }

    def __init__(self, active_state=None, boot_disk=None, boot_disk_size_gib=None, cpu_model=None, create_by=None, datacenter_id=None, external_ip_address=None, gpu_model=None, gpu_quantity=None, id=None, image_id=None, image_name=None, init_state=None, internal_ip_address=None, lcm_state=None, machine_type=None, memory=None, metadata=None, nics=None, one_state=None, price_hr=None, private_image_id=None, public_image_id=None, public_image_name=None, public_ip_address=None, region_id=None, region_name=None, renewable_energy=None, rules=None, security_group_ids=None, short_state=None, storage_disks=None, vcpus=None, vm_state=None, _configuration=None):  # noqa: E501
        """VM - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._active_state = None
        self._boot_disk = None
        self._boot_disk_size_gib = None
        self._cpu_model = None
        self._create_by = None
        self._datacenter_id = None
        self._external_ip_address = None
        self._gpu_model = None
        self._gpu_quantity = None
        self._id = None
        self._image_id = None
        self._image_name = None
        self._init_state = None
        self._internal_ip_address = None
        self._lcm_state = None
        self._machine_type = None
        self._memory = None
        self._metadata = None
        self._nics = None
        self._one_state = None
        self._price_hr = None
        self._private_image_id = None
        self._public_image_id = None
        self._public_image_name = None
        self._public_ip_address = None
        self._region_id = None
        self._region_name = None
        self._renewable_energy = None
        self._rules = None
        self._security_group_ids = None
        self._short_state = None
        self._storage_disks = None
        self._vcpus = None
        self._vm_state = None
        self.discriminator = None

        if active_state is not None:
            self.active_state = active_state
        if boot_disk is not None:
            self.boot_disk = boot_disk
        if boot_disk_size_gib is not None:
            self.boot_disk_size_gib = boot_disk_size_gib
        if cpu_model is not None:
            self.cpu_model = cpu_model
        if create_by is not None:
            self.create_by = create_by
        if datacenter_id is not None:
            self.datacenter_id = datacenter_id
        if external_ip_address is not None:
            self.external_ip_address = external_ip_address
        if gpu_model is not None:
            self.gpu_model = gpu_model
        if gpu_quantity is not None:
            self.gpu_quantity = gpu_quantity
        if id is not None:
            self.id = id
        if image_id is not None:
            self.image_id = image_id
        if image_name is not None:
            self.image_name = image_name
        if init_state is not None:
            self.init_state = init_state
        if internal_ip_address is not None:
            self.internal_ip_address = internal_ip_address
        if lcm_state is not None:
            self.lcm_state = lcm_state
        if machine_type is not None:
            self.machine_type = machine_type
        if memory is not None:
            self.memory = memory
        if metadata is not None:
            self.metadata = metadata
        if nics is not None:
            self.nics = nics
        if one_state is not None:
            self.one_state = one_state
        if price_hr is not None:
            self.price_hr = price_hr
        if private_image_id is not None:
            self.private_image_id = private_image_id
        if public_image_id is not None:
            self.public_image_id = public_image_id
        if public_image_name is not None:
            self.public_image_name = public_image_name
        if public_ip_address is not None:
            self.public_ip_address = public_ip_address
        if region_id is not None:
            self.region_id = region_id
        if region_name is not None:
            self.region_name = region_name
        if renewable_energy is not None:
            self.renewable_energy = renewable_energy
        if rules is not None:
            self.rules = rules
        if security_group_ids is not None:
            self.security_group_ids = security_group_ids
        if short_state is not None:
            self.short_state = short_state
        if storage_disks is not None:
            self.storage_disks = storage_disks
        if vcpus is not None:
            self.vcpus = vcpus
        if vm_state is not None:
            self.vm_state = vm_state

    @property
    def active_state(self):
        """Gets the active_state of this VM.  # noqa: E501


        :return: The active_state of this VM.  # noqa: E501
        :rtype: str
        """
        return self._active_state

    @active_state.setter
    def active_state(self, active_state):
        """Sets the active_state of this VM.


        :param active_state: The active_state of this VM.  # noqa: E501
        :type: str
        """

        self._active_state = active_state

    @property
    def boot_disk(self):
        """Gets the boot_disk of this VM.  # noqa: E501


        :return: The boot_disk of this VM.  # noqa: E501
        :rtype: Disk
        """
        return self._boot_disk

    @boot_disk.setter
    def boot_disk(self, boot_disk):
        """Sets the boot_disk of this VM.


        :param boot_disk: The boot_disk of this VM.  # noqa: E501
        :type: Disk
        """

        self._boot_disk = boot_disk

    @property
    def boot_disk_size_gib(self):
        """Gets the boot_disk_size_gib of this VM.  # noqa: E501


        :return: The boot_disk_size_gib of this VM.  # noqa: E501
        :rtype: int
        """
        return self._boot_disk_size_gib

    @boot_disk_size_gib.setter
    def boot_disk_size_gib(self, boot_disk_size_gib):
        """Sets the boot_disk_size_gib of this VM.


        :param boot_disk_size_gib: The boot_disk_size_gib of this VM.  # noqa: E501
        :type: int
        """

        self._boot_disk_size_gib = boot_disk_size_gib

    @property
    def cpu_model(self):
        """Gets the cpu_model of this VM.  # noqa: E501


        :return: The cpu_model of this VM.  # noqa: E501
        :rtype: str
        """
        return self._cpu_model

    @cpu_model.setter
    def cpu_model(self, cpu_model):
        """Sets the cpu_model of this VM.


        :param cpu_model: The cpu_model of this VM.  # noqa: E501
        :type: str
        """

        self._cpu_model = cpu_model

    @property
    def create_by(self):
        """Gets the create_by of this VM.  # noqa: E501


        :return: The create_by of this VM.  # noqa: E501
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        """Sets the create_by of this VM.


        :param create_by: The create_by of this VM.  # noqa: E501
        :type: str
        """

        self._create_by = create_by

    @property
    def datacenter_id(self):
        """Gets the datacenter_id of this VM.  # noqa: E501


        :return: The datacenter_id of this VM.  # noqa: E501
        :rtype: str
        """
        return self._datacenter_id

    @datacenter_id.setter
    def datacenter_id(self, datacenter_id):
        """Sets the datacenter_id of this VM.


        :param datacenter_id: The datacenter_id of this VM.  # noqa: E501
        :type: str
        """

        self._datacenter_id = datacenter_id

    @property
    def external_ip_address(self):
        """Gets the external_ip_address of this VM.  # noqa: E501


        :return: The external_ip_address of this VM.  # noqa: E501
        :rtype: str
        """
        return self._external_ip_address

    @external_ip_address.setter
    def external_ip_address(self, external_ip_address):
        """Sets the external_ip_address of this VM.


        :param external_ip_address: The external_ip_address of this VM.  # noqa: E501
        :type: str
        """

        self._external_ip_address = external_ip_address

    @property
    def gpu_model(self):
        """Gets the gpu_model of this VM.  # noqa: E501


        :return: The gpu_model of this VM.  # noqa: E501
        :rtype: str
        """
        return self._gpu_model

    @gpu_model.setter
    def gpu_model(self, gpu_model):
        """Sets the gpu_model of this VM.


        :param gpu_model: The gpu_model of this VM.  # noqa: E501
        :type: str
        """

        self._gpu_model = gpu_model

    @property
    def gpu_quantity(self):
        """Gets the gpu_quantity of this VM.  # noqa: E501


        :return: The gpu_quantity of this VM.  # noqa: E501
        :rtype: int
        """
        return self._gpu_quantity

    @gpu_quantity.setter
    def gpu_quantity(self, gpu_quantity):
        """Sets the gpu_quantity of this VM.


        :param gpu_quantity: The gpu_quantity of this VM.  # noqa: E501
        :type: int
        """

        self._gpu_quantity = gpu_quantity

    @property
    def id(self):
        """Gets the id of this VM.  # noqa: E501


        :return: The id of this VM.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VM.


        :param id: The id of this VM.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def image_id(self):
        """Gets the image_id of this VM.  # noqa: E501


        :return: The image_id of this VM.  # noqa: E501
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this VM.


        :param image_id: The image_id of this VM.  # noqa: E501
        :type: str
        """

        self._image_id = image_id

    @property
    def image_name(self):
        """Gets the image_name of this VM.  # noqa: E501


        :return: The image_name of this VM.  # noqa: E501
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        """Sets the image_name of this VM.


        :param image_name: The image_name of this VM.  # noqa: E501
        :type: str
        """

        self._image_name = image_name

    @property
    def init_state(self):
        """Gets the init_state of this VM.  # noqa: E501


        :return: The init_state of this VM.  # noqa: E501
        :rtype: str
        """
        return self._init_state

    @init_state.setter
    def init_state(self, init_state):
        """Sets the init_state of this VM.


        :param init_state: The init_state of this VM.  # noqa: E501
        :type: str
        """

        self._init_state = init_state

    @property
    def internal_ip_address(self):
        """Gets the internal_ip_address of this VM.  # noqa: E501


        :return: The internal_ip_address of this VM.  # noqa: E501
        :rtype: str
        """
        return self._internal_ip_address

    @internal_ip_address.setter
    def internal_ip_address(self, internal_ip_address):
        """Sets the internal_ip_address of this VM.


        :param internal_ip_address: The internal_ip_address of this VM.  # noqa: E501
        :type: str
        """

        self._internal_ip_address = internal_ip_address

    @property
    def lcm_state(self):
        """Gets the lcm_state of this VM.  # noqa: E501


        :return: The lcm_state of this VM.  # noqa: E501
        :rtype: str
        """
        return self._lcm_state

    @lcm_state.setter
    def lcm_state(self, lcm_state):
        """Sets the lcm_state of this VM.


        :param lcm_state: The lcm_state of this VM.  # noqa: E501
        :type: str
        """

        self._lcm_state = lcm_state

    @property
    def machine_type(self):
        """Gets the machine_type of this VM.  # noqa: E501


        :return: The machine_type of this VM.  # noqa: E501
        :rtype: str
        """
        return self._machine_type

    @machine_type.setter
    def machine_type(self, machine_type):
        """Sets the machine_type of this VM.


        :param machine_type: The machine_type of this VM.  # noqa: E501
        :type: str
        """

        self._machine_type = machine_type

    @property
    def memory(self):
        """Gets the memory of this VM.  # noqa: E501


        :return: The memory of this VM.  # noqa: E501
        :rtype: int
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this VM.


        :param memory: The memory of this VM.  # noqa: E501
        :type: int
        """

        self._memory = memory

    @property
    def metadata(self):
        """Gets the metadata of this VM.  # noqa: E501


        :return: The metadata of this VM.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this VM.


        :param metadata: The metadata of this VM.  # noqa: E501
        :type: dict(str, str)
        """

        self._metadata = metadata

    @property
    def nics(self):
        """Gets the nics of this VM.  # noqa: E501


        :return: The nics of this VM.  # noqa: E501
        :rtype: list[VMNIC]
        """
        return self._nics

    @nics.setter
    def nics(self, nics):
        """Sets the nics of this VM.


        :param nics: The nics of this VM.  # noqa: E501
        :type: list[VMNIC]
        """

        self._nics = nics

    @property
    def one_state(self):
        """Gets the one_state of this VM.  # noqa: E501


        :return: The one_state of this VM.  # noqa: E501
        :rtype: str
        """
        return self._one_state

    @one_state.setter
    def one_state(self, one_state):
        """Sets the one_state of this VM.


        :param one_state: The one_state of this VM.  # noqa: E501
        :type: str
        """

        self._one_state = one_state

    @property
    def price_hr(self):
        """Gets the price_hr of this VM.  # noqa: E501


        :return: The price_hr of this VM.  # noqa: E501
        :rtype: float
        """
        return self._price_hr

    @price_hr.setter
    def price_hr(self, price_hr):
        """Sets the price_hr of this VM.


        :param price_hr: The price_hr of this VM.  # noqa: E501
        :type: float
        """

        self._price_hr = price_hr

    @property
    def private_image_id(self):
        """Gets the private_image_id of this VM.  # noqa: E501


        :return: The private_image_id of this VM.  # noqa: E501
        :rtype: str
        """
        return self._private_image_id

    @private_image_id.setter
    def private_image_id(self, private_image_id):
        """Sets the private_image_id of this VM.


        :param private_image_id: The private_image_id of this VM.  # noqa: E501
        :type: str
        """

        self._private_image_id = private_image_id

    @property
    def public_image_id(self):
        """Gets the public_image_id of this VM.  # noqa: E501


        :return: The public_image_id of this VM.  # noqa: E501
        :rtype: str
        """
        return self._public_image_id

    @public_image_id.setter
    def public_image_id(self, public_image_id):
        """Sets the public_image_id of this VM.


        :param public_image_id: The public_image_id of this VM.  # noqa: E501
        :type: str
        """

        self._public_image_id = public_image_id

    @property
    def public_image_name(self):
        """Gets the public_image_name of this VM.  # noqa: E501


        :return: The public_image_name of this VM.  # noqa: E501
        :rtype: str
        """
        return self._public_image_name

    @public_image_name.setter
    def public_image_name(self, public_image_name):
        """Sets the public_image_name of this VM.


        :param public_image_name: The public_image_name of this VM.  # noqa: E501
        :type: str
        """

        self._public_image_name = public_image_name

    @property
    def public_ip_address(self):
        """Gets the public_ip_address of this VM.  # noqa: E501


        :return: The public_ip_address of this VM.  # noqa: E501
        :rtype: str
        """
        return self._public_ip_address

    @public_ip_address.setter
    def public_ip_address(self, public_ip_address):
        """Sets the public_ip_address of this VM.


        :param public_ip_address: The public_ip_address of this VM.  # noqa: E501
        :type: str
        """

        self._public_ip_address = public_ip_address

    @property
    def region_id(self):
        """Gets the region_id of this VM.  # noqa: E501


        :return: The region_id of this VM.  # noqa: E501
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this VM.


        :param region_id: The region_id of this VM.  # noqa: E501
        :type: str
        """

        self._region_id = region_id

    @property
    def region_name(self):
        """Gets the region_name of this VM.  # noqa: E501


        :return: The region_name of this VM.  # noqa: E501
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        """Sets the region_name of this VM.


        :param region_name: The region_name of this VM.  # noqa: E501
        :type: str
        """

        self._region_name = region_name

    @property
    def renewable_energy(self):
        """Gets the renewable_energy of this VM.  # noqa: E501


        :return: The renewable_energy of this VM.  # noqa: E501
        :rtype: bool
        """
        return self._renewable_energy

    @renewable_energy.setter
    def renewable_energy(self, renewable_energy):
        """Sets the renewable_energy of this VM.


        :param renewable_energy: The renewable_energy of this VM.  # noqa: E501
        :type: bool
        """

        self._renewable_energy = renewable_energy

    @property
    def rules(self):
        """Gets the rules of this VM.  # noqa: E501


        :return: The rules of this VM.  # noqa: E501
        :rtype: list[SecurityGroupRule]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this VM.


        :param rules: The rules of this VM.  # noqa: E501
        :type: list[SecurityGroupRule]
        """

        self._rules = rules

    @property
    def security_group_ids(self):
        """Gets the security_group_ids of this VM.  # noqa: E501


        :return: The security_group_ids of this VM.  # noqa: E501
        :rtype: list[str]
        """
        return self._security_group_ids

    @security_group_ids.setter
    def security_group_ids(self, security_group_ids):
        """Sets the security_group_ids of this VM.


        :param security_group_ids: The security_group_ids of this VM.  # noqa: E501
        :type: list[str]
        """

        self._security_group_ids = security_group_ids

    @property
    def short_state(self):
        """Gets the short_state of this VM.  # noqa: E501


        :return: The short_state of this VM.  # noqa: E501
        :rtype: str
        """
        return self._short_state

    @short_state.setter
    def short_state(self, short_state):
        """Sets the short_state of this VM.


        :param short_state: The short_state of this VM.  # noqa: E501
        :type: str
        """

        self._short_state = short_state

    @property
    def storage_disks(self):
        """Gets the storage_disks of this VM.  # noqa: E501


        :return: The storage_disks of this VM.  # noqa: E501
        :rtype: list[Disk]
        """
        return self._storage_disks

    @storage_disks.setter
    def storage_disks(self, storage_disks):
        """Sets the storage_disks of this VM.


        :param storage_disks: The storage_disks of this VM.  # noqa: E501
        :type: list[Disk]
        """

        self._storage_disks = storage_disks

    @property
    def vcpus(self):
        """Gets the vcpus of this VM.  # noqa: E501


        :return: The vcpus of this VM.  # noqa: E501
        :rtype: int
        """
        return self._vcpus

    @vcpus.setter
    def vcpus(self, vcpus):
        """Sets the vcpus of this VM.


        :param vcpus: The vcpus of this VM.  # noqa: E501
        :type: int
        """

        self._vcpus = vcpus

    @property
    def vm_state(self):
        """Gets the vm_state of this VM.  # noqa: E501


        :return: The vm_state of this VM.  # noqa: E501
        :rtype: VmState
        """
        return self._vm_state

    @vm_state.setter
    def vm_state(self, vm_state):
        """Sets the vm_state of this VM.


        :param vm_state: The vm_state of this VM.  # noqa: E501
        :type: VmState
        """

        self._vm_state = vm_state

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
        if issubclass(VM, dict):
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
        if not isinstance(other, VM):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VM):
            return True

        return self.to_dict() != other.to_dict()
