# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from bedrock.mozorg.util import page

urlpatterns = (
    page('privacy-policy', 'persona/privacy-policy.html'),
    page('terms-of-service', 'persona/terms-of-service.html'),
)
