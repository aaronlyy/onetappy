# api.py
# https://www.onetap.com/threads/cloud-api.37180/
# Author: Aaron Levi (https://github.com/aaronlyy)
# Repo: https://github.com/aaronlyy/onetappy

import requests

# TODO:
# add all endpoint methods
# add custom exceptions

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

        self._base_url = "https://api.onetap.com/cloud"

# region base request method
    def _req(self, method:str, endpoint:str, data:dict=None):
        url = f"{self._base_url}{endpoint}"

        if method == "GET":
            return requests.get(url, headers=self._headers).json()
        elif method == "POST":
            return requests.post(url, headers=self._headers, data=data).json()
        elif method == "DELETE":
            if data:
                return requests.delete(url, headers=self._headers, data=data).json()
            else:
                return requests.delete(url, headers=self._headers).json()
        else:
            raise Exception
# endregion

# region configs
    def get_all_configs(self):
        """Gets all configs.
        """
        endpoint = "/configs/"
        return self._req("GET", endpoint)

    def create_config(self, name:str, data:str):
        """Creates a new config.

        Args:
            name (str): Name of the config.
            data (str): Config content data.
        """
        endpoint = f"/configs/"
        d = {
            "name": name,
            "data": data
        }
        return self._req("POST", endpoint, data=d)

    def get_config(self, config_id:str):
        """Gets a specific config.

        Args:
            config_id (str): ID of the config.
        """
        endpoint = f"/configs/{config_id}"
        return self._req("GET", endpoint)

    def update_config(self, config_id:int, name:str, data:str):
        """Updates an existing config.

        Args:
            config_id (int): ID of the config
            name (str): Name of the config
            data (str): Config content data
        """
        endpoint = f"/configs/{config_id}"
        d = {
            "name": name,
            "data": data
        }
        return self._req("POST", endpoint, data=d)

    def delete_config(self, config_id:int):
        """Deletes an existing config.

        Args:
            config_id (int): ID of the config
        """
        endpoint = f"/configs/{config_id}"
        return self._req("DELETE", endpoint)
# endregion

# region config invites
    def get_all_config_invites(self):
        """Gets all config invites.
        """
        endpoint = f"/configs/invites"
        return self._req("GET", endpoint)

    def get_config_invites(self, config_id:int):
        """Gets all invites for a specific config.

        Args:
            config_id (int): ID of config
        """
        endpoint = f"/configs/{config_id}/invites"
        return self._req("GET", endpoint)

    def create_config_invite(self, config_id:int, max_age:int, max_uses:int):
        """Creates a new config invite.

        Args:
            config_id (int): ID of config
            max_age (int): Maximum age. 1 = 1h, 2 = 3h, 3 = 6h, 4 = 12h, 5 = 24h, 6 = 48h
            max_uses (int): Maximum uses. 1 = 1, 2 = 5, 3 = 10, 4 = 25, 5 = 50, 6 = 100
        """
        endpoint = f"/configs/{config_id}/invites"
        d = {
            "max_age": max_age,
            "max_uses": max_uses
        }
        return self._req("POST", endpoint, data=d)

    def delete_config_invite(self, config_id:int, invite_id:int):
        """Deletes a config invite.

        Args:
            config_id (int): ID of config.
            invite_id (int): ID of the config invite to delete.
        """
        endpoint = f"/configs/{config_id}/invites"
        d = {
            "invite_id": invite_id
        }
        return self._req("DELETE", endpoint, data=d)
# endregion

# region config subscription
    def get_all_config_subs(self):
        """Gets all config subscriptions.
        """
        endpoint = f"/configs/subscriptions"
        return self._req("GET", endpoint)

    def get_config_subs(self, config_id:int):
        """Gets all subscriptions for a specific config.

        Args:
            config_id (int): ID of config.
        """
        endpoint = f"/configs/{config_id}/subscriptions"
        return self._req("GET", endpoint)

    def create_config_sub(self, config_id:int, user_id:int):
        """Creates a new config subscription.

        Args:
            config_id (int): ID of config.
            user_id (int): ID of the user to share the config with.
        """
        endpoint = f"/configs/{config_id}/subscriptions"
        d = {
            "user_id": user_id
        }
        return self._req("POST", endpoint, data=d)

    def delete_config_sub(self, config_id:int, user_id:int):
        """Deletes a config subscription.

        Args:
            config_id (int): ID of config.
            user_id (int):  ID of the user to stop sharing the config with.
        """
        endpoint = f"/configs/{config_id}/subscriptions"
        d = {
            "user_id": user_id
        }
        return self._req("DELETE", endpoint, data=d)
# endregion

# region scripts
    def get_all_scripts(self):
        """Gets all scripts.
        """
        endpoint = f"/scripts/"
        return self._req("GET", endpoint)
    
    def get_script(self, script_id:int):
        """Gets a specific script.

        Args:
            script_id (int): ID of script.
        """
        endpoint = f"/scripts/{script_id}/"
        return self._req("GET", endpoint)

    def update_script(self, script_id:int, name:str):
        """Updates an existing script.

        Args:
            script_id (int): ID of script.
            name (str): Name of the script.
        """
        endpoint = f"/scripts/{script_id}/"
        d = {
            "name": name
        }
        return self._req("POST", endpoint, data=d)

    def delete_script(self, script_id:int):
        """Deletes an existing script.

        Args:
            script_id (int): ID of script.
        """
        endpoint = f"/scripts/{script_id}/"
        return self._req("DELETE", endpoint)
# endregion

# region script invites
    def get_all_script_invites(self):
        """Gets all script invites.
        """
        endpoint = f"/scripts/invites/"
        return self._req("GET", endpoint)

    def get_script_invites(self, script_id:int):
        """Gets all invites for a specific script.

        Args:
            script_id (int): ID of script.
        """
        endpoint = f"/scripts/{script_id}/invites"
        return self._req("GET", endpoint)

    def create_script_invite(self, script_id:int, max_age:int, max_uses:int):
        """Creates a new script invite.

        Args:
            script_id (int): ID of script.
            max_age (int): Maximum age. 1 = 1h, 2 = 3h, 3 = 6h, 4 = 12h, 5 = 24h, 6 = 48h
            max_uses (int): Maximum uses. 1 = 1, 2 = 5, 3 = 10, 4 = 25, 5 = 50, 6 = 100
        """
        endpoint = f"/scripts/{script_id}/invites"
        d = {
            "max_age": max_age,
            "max_uses": max_uses
        }
        return self._req("POST", endpoint, data=d)

    def delete_script_invite(self, script_id:int, invite_id:int):
        """Deletes a config invite.

        Args:
            script_id (int): ID of script.
            invite_id (int): ID of the config to delete.
        """
        endpoint = f"/scripts/{script_id}"
        d = {
            "invite_id": invite_id
        }
        return self._req("DELETE", endpoint, data=d)
# endregion

# region script subscriptions
    def get_all_script_subs(self):
        """Gets all config subscriptions.
        """
        pass
    
    def get_script_subs(self, script_id:int):
        """Gets all subscriptions for a specific config.

        Args:
            script_id (int): ID of script.
        """
        pass

    def create_script_sub(self, script_id:int, user_id:int):
        """Creates a new config subscription.

        Args:
            script_id (int): ID of script.
            user_id (int): ID of the user to share the script with.
        """
        pass

    def delete_script_sub(self, script_id:int, user_id:int):
        """Deletes a script subscription.

        Args:
            script_id (int): ID of script.
            user_id (int): ID of the user to stop sharing the script with.
        """
        pass
# endregion

# endregion