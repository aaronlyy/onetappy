# api.py
# https://www.onetap.com/threads/cloud-api.37180/
# Author: Aaron Levi (aaronlyy)
# Repo: https://github.com/aaronlyy/onetappy
# v0.1

import requests

# TODO:
# add methods: 

# region base class
class Onetappy:
    """GET, POST or DELETE configs from/to the cloud.
    """

    def __init__(self, api_id:str, api_secret:str, api_key:str):
        self._headers = {
            "X-Api-Id": api_id,
            "X-Api-Secret": api_secret,
            "X-Api-Key": api_key
        }

        self._base_url = "https://api.onetap.com/cloud/"

# region base request method
    def _req(self, endpoint:str, method:str, data:dict=None):
        url = f"{self._base_url}{endpoint}"

        if method == "GET":
            return requests.get(url, headers=self._headers)
        elif method == "POST":
            return requests.post(url, headers=self._headers, data=data)
        elif method == "DELETE":
            pass
        else:
            raise Exception
# endregion

# region configs
    def get_configs(self):
        """Gets all configs
        """
        endpoint = "configs/"
        res = self._req(endpoint, "GET")
        return OnetappyResponse(res)

    def create_config(self, name:str, data:str):
        """Creates a new config.

        Args:
            name (str): Name of the config
            data (str): Config content data
        """
        pass

    def get_config(self, config_id:str):
        """Gets a specific config.

        Args:
            config_id (str): ID of the config
        """
        endpoint = f"configs/{config_id}"
        res = self._req(endpoint, "GET")
        return OnetappyResponse(res)

    def update_config(self, config_id:int, name:str, data:str):
        """Updates an existing config.

        Args:
            config_id (int): ID of the config
            name (str): Name of the config
            data (str): Config content data
        """
        pass

    def delete_config(self, config_id:int):
        """Deletes an existing config.

        Args:
            config_id (int): ID of teh config
        """
        pass
# endregion

# region config invites
    def get_config_invites(self):
        pass

    def get_config_invite(self, config_id:int):
        pass

    def create_config_invite(self, config_id:int, max_age:int, max_uses:int):
        pass

    def delete_config_invite(self, config_id:int, invite_id:int):
        pass
# endregion

# region config subscription
    def get_all_config_subs(self):
        pass

    def get_config_subs(self, config_id:int):
        pass

    def create_config_sub(self, config_id:int, user_id:int):
        pass

    def delete_config_sub(self, config_id:int, user_id:int):
        pass
# endregion

# region scripts
    def get_scripts(self):
        pass
    
    def get_script(self, script_id:int):
        pass

    def update_script(self, script_id:int, name:str):
        pass

    def delete_script(self, script_id:int):
        pass
# endregion

# region script invite
    def get_all_script_invites(self):
        pass

    def get_script_invites(self, script_id:int):
        pass

    def create_script_invite(self, script_id:int, max_age:int, max_uses:int):
        pass

    def delete_script_invite(self, script_id:int, invite_id:int):
        pass
# endregion

# region script subscriptions
    def get_all_script_subs(self):
        pass
    
    def get_script_subs(self, script_id:int):
        pass

    def create_script_sub(self, script_id:int, user_id:int):
        pass

    def delete_script_sub(self, script_id:int, user_id:int):
        pass
# endregion

# endregion

# region response class
class OnetappyResponse:
    def __init__(self, res):
        self._json = res.json()

    def json(self):
        return self._json

    def __getattr__(self, attr):
        if attr in self._json:
            return attr
        else:
            return None
# endregion