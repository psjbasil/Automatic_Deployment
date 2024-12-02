# services/service_manager.py
from services.docker_utils import deploy_container, stop_container

class ServiceManager:
    def __init__(self):
        self.services = {}

    def deploy_service(self, host_ip, service_name, image_name, ports, environment=None):
        """部署服务"""
        service_id = deploy_container(host_ip, service_name, image_name, ports, environment)
        self.services[service_name] = service_id
        return service_id

    def stop_service(self, service_name):
        """停止服务"""
        if service_name in self.services:
            service_id = self.services.pop(service_name)
            stop_container(service_id)
        else:
            print(f"Service {service_name} not found.")

# 示例用法
if __name__ == "__main__":
    manager = ServiceManager()
    # 部署Web服务器
    web_service_id = manager.deploy_service('192.168.1.100', 'webserver', 'nginx', {'80/tcp': 80})
    # 停止Web服务器
    manager.stop_service('webserver')