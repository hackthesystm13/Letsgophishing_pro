import pytest
from unittest.mock import patch, MagicMock

from msf_wrapper.client import MetasploitManager

@patch('msf_wrapper.client.MsfRpcClient')
@patch('msf_wrapper.client._port_open', return_value=True)
def test_run_module(mock_port_open, mock_msfclient_cls):
    mock_client = MagicMock()
    mock_mod = MagicMock()
    mock_mod.execute.return_value = 123
    mock_client.modules.use.return_value = mock_mod
    mock_msfclient_cls.return_value = mock_client

    m = MetasploitManager(auto_start_container=False)
    job = m.run_module('exploit', 'dummy/exploit')
    assert job == 123

@patch('msf_wrapper.client._port_open', return_value=False)
@patch('msf_wrapper.client.subprocess.run')
def test_auto_start_container_starts_docker(mock_subproc_run, mock_port_open):
    mock_proc = MagicMock()
    mock_proc.returncode = 0
    mock_subproc_run.return_value = mock_proc

    with patch('msf_wrapper.client.MsfRpcClient') as mock_msfclient_cls:
        with patch('msf_wrapper.client._port_open', side_effect=[False, True]):
            mock_client = MagicMock()
            mock_mod = MagicMock()
            mock_mod.execute.return_value = 456
            mock_client.modules.use.return_value = mock_mod
            mock_msfclient_cls.return_value = mock_client

            m = MetasploitManager(auto_start_container=True, connect_timeout=5)
            job = m.run_module('exploit', 'dummy/exploit')
            assert job == 456
            assert mock_subproc_run.called
