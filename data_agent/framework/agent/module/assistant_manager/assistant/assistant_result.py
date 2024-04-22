from typing import Any

from data_agent.framework.action.action_result import ActionResult


class AssistantResult:
    result: ActionResult = None
    output: Any = None

    def __init__(self, result: ActionResult, output: Any):
        self.result = result
        self.output = output
