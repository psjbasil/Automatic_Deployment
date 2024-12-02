# services/docker_utils.py
import docker
from docker.models.containers import Container

client = docker.from_env()

def deploy_container(host_ip, service_name, image_name, ports, environment=None):
    """在指定主机上部署Docker容器"""
    container = client.containers.run(
        image=image_name,
        detach=True,
        name=service_name,
        ports=ports,
        environment=environment or {},
        network_mode="host"
    )
    return container.id

def stop_container(service_id):
    """停止并移除Docker容器"""
    try:
        container: Container = client.containers.get(service_id)
        container.stop()
        container.remove()
    except Exception as e:
        print(f"Error stopping container {service_id}: {e}")