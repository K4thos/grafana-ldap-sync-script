import logging
import yaml

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("grafana-ldap-sync-script")

class config:
    GRAFANA_AUTH = ""
    GRAFANA_URL = ""
    GRAFANA_PROTOCOL = "http"

    LDAP_SERVER_URL = ""
    LDAP_PORT = ""
    LDAP_USER = ""
    LDAP_PASSWORD = ""
    LDAP_GROUP_SEARCH_BASE = ""
    LDAP_GROUP_DESCRIPTOR = ""
    LDAP_GROUP_SEARCH_FILTER = ""
    LDAP_MEMBER_ATTRIBUTE = ""
    LDAP_IS_NTLM = False
    LDAP_USE_SSL = False
    LDAP_USER_LOGIN_ATTRIBUTE = ""
    LDAP_USER_NAME_ATTRIBUTE = ""
    LDAP_USER_MAIL_ATTRIBUTE = ""
    LDAP_USER_SEARCH_BASE = ""
    LDAP_USER_SEARCH_FILTER = ""
    DRY_RUN = False

    def __init__(self, config_path):
        self.load_config(config_path)

    def load_config(self, config_path):
        """
        Loads the config file present at the given path and fills all class variables with the defined config.
        """
        try:
            with open(config_path) as f:
                config = yaml.safe_load(f)["config"]
        except FileNotFoundError as e:
            logger.error("Config file %s does not exist!", config_path)
            raise e
        except Exception as e:
            logger.error("Error reading config file %s: %s", config_path, str(e))
            raise e
        self.GRAFANA_AUTH = (
            config["grafana"]["user"],
            config["grafana"]["password"]
        )
        self.GRAFANA_URL = config["grafana"]["url"]
        if config["grafana"]["protocol"]:
            self.GRAFANA_PROTOCOL = config["grafana"]["protocol"]

        self.LDAP_SERVER_URL = config["ldap"]["url"]
        self.LDAP_PORT = config["ldap"]["port"]
        self.LDAP_USER = config["ldap"]["login"]
        self.LDAP_PASSWORD = config["ldap"]["password"]
        self.LDAP_GROUP_SEARCH_BASE = config["ldap"]["groupSearchBase"]
        self.LDAP_GROUP_SEARCH_FILTER = config["ldap"]["groupSearchFilter"]
        self.LDAP_MEMBER_ATTRIBUTE = config["ldap"]["memberAttributeName"]
        self.LDAP_IS_NTLM = config["ldap"]["useNTLM"]
        self.LDAP_USE_SSL = config["ldap"]["useSSL"]
        self.LDAP_USER_LOGIN_ATTRIBUTE = config["ldap"]["userLoginAttribute"]
        self.LDAP_USER_NAME_ATTRIBUTE = config["ldap"]["userNameAttribute"]
        self.LDAP_USER_MAIL_ATTRIBUTE = config["ldap"]["userMailAttribute"]
        self.LDAP_USER_SEARCH_BASE = config["ldap"]["userSearchBase"]
        self.LDAP_USER_SEARCH_FILTER = config["ldap"]["userSearchFilter"]