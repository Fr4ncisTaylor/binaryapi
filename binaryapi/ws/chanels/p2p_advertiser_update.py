"""Module for Binary p2p_advertiser_update websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#p2p_advertiser_update

class P2PAdvertiserUpdate(Base):
    """Class for Binary p2p_advertiser_update websocket chanel."""

    name = "p2p_advertiser_update"

    def __call__(self, contact_info: str=None, default_advert_description: str=None, is_listed: int=None, name: str=None, payment_info: str=None, passthrough=None, req_id: int=None):
        """Method to send message to p2p_advertiser_update websocket chanel.
        P2P Advertiser Update (request)
        Update the information of the P2P advertiser for the current account. Can only be used by an approved P2P advertiser. **This API call is still in Beta.**
        :param contact_info: [Optional] Advertiser's contact information, to be used as a default for new sell adverts.
        :type contact_info: str
        :param default_advert_description: [Optional] Default description that can be used every time an advert is created.
        :type default_advert_description: str
        :param is_listed: [Optional] Used to set if the advertiser's adverts could be listed. When `0`, adverts won't be listed regardless of they are active or not. This doesn't change the `is_active` of each individual advert.
        :type is_listed: int
        :param name: [Optional] The advertiser's displayed name.
        :type name: str
        :param payment_info: [Optional] Advertiser's payment information, to be used as a default for new sell adverts.
        :type payment_info: str
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "p2p_advertiser_update": 1
        }

        if contact_info:
            data['contact_info'] = contact_info

        if default_advert_description:
            data['default_advert_description'] = default_advert_description

        if is_listed:
            data['is_listed'] = is_listed

        if name:
            data['name'] = name

        if payment_info:
            data['payment_info'] = payment_info

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)