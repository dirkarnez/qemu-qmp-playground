            qmp = QMPClient()
            try:
                await qmp.connect((str(self.qmp_addr), int(self.qmp_port)))
                response = await qmp.execute(execute, arguments=arguments)
            finally:
                await qmp.disconnect()

python3 -m venv venv
. ./venv/bin/activate
pip3 install ${QEMU_SRC_PATH}/python/
