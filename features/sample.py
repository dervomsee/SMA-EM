"""
 * Feature-Module for SMA-EM daemon
 * sample class for features
 * just an example
 * by Wenger Florian 2018-05-27
 *
 *
 *  this software is released under GNU General Public License, version 2.
 *  This program is free software;
 *  you can redistribute it and/or modify it under the terms of the GNU General Public License
 *  as published by the Free Software Foundation; version 2 of the License.
 *  This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
 *  without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 *  See the GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License along with this program;
 *  if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
 *
 */
"""



from features.smafeature import smafeature
class feature(smafeature):
    def __init__(self):
        super().__init__()
        #declare your own thins
        print("initialisation of feature sample")
    def run (self,emparts):
        # my configs
        #config=self.getconfig()
        # do something
        print(('%.4f' % emparts['pregard']))
        #serial=format(emparts['serial'])
    def cleanup(self):
        print("cleanup housekeeping of feature... nothing to do @cleanup")