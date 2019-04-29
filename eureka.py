from py_eureka_client import eureka_client


def eureka():
    eureka_client.init(eureka_server="http://localhost:7080/eureka",
                       app_name="neural-network",
                       instance_port=5000,
                       is_coordinating_discovery_server=True)
