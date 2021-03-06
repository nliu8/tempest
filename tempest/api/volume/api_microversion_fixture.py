#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import fixtures

from tempest.services.volume.base import base_v3_client


class APIMicroversionFixture(fixtures.Fixture):

    def __init__(self, volume_microversion):
        self.volume_microversion = volume_microversion

    def _setUp(self):
        super(APIMicroversionFixture, self)._setUp()
        base_v3_client.VOLUME_MICROVERSION = self.volume_microversion
        self.addCleanup(self._reset_volume_microversion)

    def _reset_volume_microversion(self):
        base_v3_client.VOLUME_MICROVERSION = None
