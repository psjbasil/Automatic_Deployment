# network/sdn_controller.py
def configure_flow(src_service, dst_service, protocol, action):
    """向SDN控制器添加或删除流规则"""
    print(f"Configuring flow from {src_service} to {dst_service}, protocol: {protocol}, action: {action}")
    # 实际代码应该包含向控制器发送请求的逻辑
    # 例如，使用Ryu REST API或其他方式与控制器交互