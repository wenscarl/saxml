# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Base class for servable model configs."""

import abc
from typing import Any, Dict, List, Optional, Union, Type

from saxml.server import utils


class ServableMethodParams(metaclass=abc.ABCMeta):
  """A base config class for a method."""

  @abc.abstractmethod
  def get_batch_size(self) -> Union[int, List[int]]:
    """Returns the static batch size or a list of allowed batch sizes."""

  @abc.abstractmethod
  def get_max_live_batches(self) -> int:
    """Returns the maximum number of batches in queue for this method."""

  @abc.abstractmethod
  def get_default_extra_inputs(self) -> Optional[Dict[str, float]]:
    """Returns the default values for extra inputs.

    Extra inputs are a dictionary of {key: default_value} pairs. The input for a
    function is a NestedMap. The `key` in `extra_inputs` can be one of the key
    in the input. The `default_value` is the default value for input[key].
    """


class ServableModelParams(metaclass=abc.ABCMeta):
  """A base class that each model config needs to implement for serving."""

  @classmethod
  @abc.abstractmethod
  def check_serving_platform(cls) -> utils.Status:
    """Returns OK status if the current platform supports this model."""

  @abc.abstractmethod
  def load(self, model_key: str, checkpoint_path: str, primary_process_id: int,
           prng_key: int) -> Any:
    """Loads and returns the ServableModel."""

  @abc.abstractmethod
  def methods(self) -> Dict[str, ServableMethodParams]:
    """Returns a dict of {name, method params}."""


ServableModelParamsT = Type[ServableModelParams]
