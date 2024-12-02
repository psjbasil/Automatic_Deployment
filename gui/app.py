# gui/app.py
import tkinter as tk
from tkinter import messagebox, simpledialog
from services.service_manager import ServiceManager
from network.sdn_controller import configure_flow


class ServiceManagerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Service Manager")

        # 初始化服务管理器
        self.service_manager = ServiceManager()

        # 主机列表
        self.hosts = ["192.168.1.100", "192.168.1.101"]

        # 创建GUI元素
        self.create_widgets()

    def create_widgets(self):
        # 选择主机
        self.label_host = tk.Label(self, text="Choose a host:")
        self.label_host.pack(pady=5)
        self.host_var = tk.StringVar(value=self.hosts[0])
        self.host_menu = tk.OptionMenu(self, self.host_var, *self.hosts)
        self.host_menu.pack(pady=5)

        # 服务名称输入框
        self.label_service = tk.Label(self, text="Enter service name:")
        self.label_service.pack(pady=5)
        self.service_entry = tk.Entry(self)
        self.service_entry.pack(pady=5)

        # 部署按钮
        self.deploy_button = tk.Button(self, text="Deploy Service", command=self.deploy_service)
        self.deploy_button.pack(pady=5)

        # 停止按钮
        self.stop_button = tk.Button(self, text="Stop Service", command=self.stop_service)
        self.stop_button.pack(pady=5)

        # 设置应用间通信
        self.label_communication = tk.Label(self, text="Set communication between applications:")
        self.label_communication.pack(pady=5)
        self.src_service_label = tk.Label(self, text="Source Service Name:")
        self.src_service_label.pack(pady=5)
        self.src_service_entry = tk.Entry(self)
        self.src_service_entry.pack(pady=5)
        self.dst_service_label = tk.Label(self, text="Destination Service Name:")
        self.dst_service_label.pack(pady=5)
        self.dst_service_entry = tk.Entry(self)
        self.dst_service_entry.pack(pady=5)
        self.set_communication_button = tk.Button(self, text="Set Communication", command=self.set_communication)
        self.set_communication_button.pack(pady=5)

    def deploy_service(self):
        """部署服务"""
        host_ip = self.host_var.get()
        service_name = self.service_entry.get().strip()
        if not service_name:
            messagebox.showerror("Input Error", "Please enter a valid service name.")
            return

        try:
            # 这里假设我们部署的是Nginx作为Web服务器
            service_id = self.service_manager.deploy_service(host_ip, service_name, 'nginx', {'80/tcp': 80})
            messagebox.showinfo("Success", f"Service {service_name} deployed with ID: {service_id}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def stop_service(self):
        """停止服务"""
        service_name = self.service_entry.get().strip()
        if not service_name:
            messagebox.showerror("Input Error", "Please enter a valid service name.")
            return

        try:
            self.service_manager.stop_service(service_name)
            messagebox.showinfo("Success", f"Service {service_name} stopped and removed.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def set_communication(self):
        """设置应用间的通信要求并配置相应的流规则"""
        src_service = self.src_service_entry.get().strip()
        dst_service = self.dst_service_entry.get().strip()
        if not (src_service and dst_service):
            messagebox.showerror("Input Error", "Please enter both source and destination service names.")
            return

        try:
            # 这里假设每个服务都有一个默认的端口80
            configure_flow(src_service, dst_service, 'tcp', 'allow')
            messagebox.showinfo("Success", f"Communication allowed from {src_service} to {dst_service}.")
        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    app = ServiceManagerApp()
    app.mainloop()