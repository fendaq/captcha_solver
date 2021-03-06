# Copyright 2018 Northwest University
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from .base_options import BaseOptions

class TuneOptions(BaseOptions):
    def initialize(self):
        BaseOptions.initialize(self)
        self.parser.add_argument('--base_model_name', type=str, default='google-improvement-02-0.18.hdf5',
                                 help='which model to load')
        self.parser.add_argument('--nb_retain_layers', type=int, default=8, help='number of former layers to be retained')
        self.parser.add_argument('--epoch', type=int, default=50, help='number of epoch')
        self.parser.add_argument('--lr', type=float, default=0.0001, help='initial learning rate of loss function')
        self.parser.add_argument('--phase', type=str, default='val', help='the dataset folder, e.g. train, test, val')
        self.parser.add_argument('--plot', action='store_true', default=False, help='plot val_acc and val_loss figure')

        self.isTrain = False
