import sys
import os
import pytest
from unittest.mock import Mock

# Añadir el directorio del proyecto al path para poder importar `taskmanager`
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from taskmanager import TaskManager, Task


def make_manager_without_io(monkeypatch):
    # Evitar que __init__ intente leer fichero
    monkeypatch.setattr(TaskManager, "load_tasks", lambda self: None)
    mgr = TaskManager()
    # Aseguramos estado limpio
    mgr._tasks = []
    mgr._next_id = 1
    return mgr


def test_add_task_calls_save_and_prints(monkeypatch, capsys):
    manager = make_manager_without_io(monkeypatch)
    save_mock = Mock()
    monkeypatch.setattr(manager, "save_tasks", save_mock)

    manager.add_task("Comprar leche")

    assert len(manager._tasks) == 1
    assert manager._tasks[0].description == "Comprar leche"
    save_mock.assert_called_once()
    out = capsys.readouterr().out
    assert "Tarea añadida: Comprar leche" in out


def test_complete_existing_task_marks_and_calls_save(monkeypatch, capsys):
    manager = make_manager_without_io(monkeypatch)
    manager._tasks = [Task(1, "Tarea1"), Task(2, "Tarea2")] 
    save_mock = Mock()
    monkeypatch.setattr(manager, "save_tasks", save_mock)

    manager.complete_task(2)

    assert manager._tasks[1].completed is True
    save_mock.assert_called_once()
    out = capsys.readouterr().out
    assert "Tarea completada:" in out


def test_complete_nonexistent_task_prints_not_found_and_no_save(monkeypatch, capsys):
    manager = make_manager_without_io(monkeypatch)
    manager._tasks = [Task(1, "Solo")] 
    save_mock = Mock()
    monkeypatch.setattr(manager, "save_tasks", save_mock)

    manager.complete_task(99)

    save_mock.assert_not_called()
    out = capsys.readouterr().out.strip()
    assert out == "Tarea no encontrada: #99"


def test_delete_existing_task_removes_and_calls_save(monkeypatch, capsys):
    manager = make_manager_without_io(monkeypatch)
    manager._tasks = [Task(1, "Primera"), Task(2, "Segunda")]
    save_mock = Mock()
    monkeypatch.setattr(manager, "save_tasks", save_mock)

    manager.delete_task(1)

    assert len(manager._tasks) == 1
    assert manager._tasks[0].id == 2
    save_mock.assert_called_once()
    out = capsys.readouterr().out
    assert "Tarea eliminada: #1" in out


def test_delete_nonexistent_task_prints_buggy_message_and_no_save(monkeypatch, capsys):
    # El código actual imprime la cadena literal "Tarea no encontrada: #{id}"
    manager = make_manager_without_io(monkeypatch)
    manager._tasks = [Task(1, "Solo")]
    save_mock = Mock()
    monkeypatch.setattr(manager, "save_tasks", save_mock)

    manager.delete_task(99)

    save_mock.assert_not_called()
    out = capsys.readouterr().out.strip()
    assert out == "Tarea no encontrada: #{id}"
