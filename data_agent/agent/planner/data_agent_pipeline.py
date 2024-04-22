from typing import List

from data_agent.agent.assistants.assistant_keys import AssistantKeys
from data_agent.agent.assistants.sql_assistant.sql_assistant import (
    SqlAssistant,
    SqlAssistantParams,
)
from data_agent.agent.planner.data_agent_planner_params import DataAgentPlannerParams
from data_agent.framework.agent.context import Context
from data_agent.framework.agent.module.assistant_manager.assistant.assistant import (
    Assistant,
)
from data_agent.framework.agent.module.planner.pipeline.pipeline import Pipeline


class DataAgentPipeline(Pipeline[DataAgentPlannerParams, str]):
    def end(self, assistant: Assistant):
        pass

    def start(self, assistant: type[Assistant]) -> Assistant:
        if assistant is SqlAssistant:
            return SqlAssistant(SqlAssistantParams(**vars(self.params)), self.context)

    def __init__(self, params: DataAgentPlannerParams, context: Context):
        super().__init__(params, context)

    def init(self) -> List[type(Assistant)]:
        return [self.context.get_assistant(AssistantKeys.SQL_ASSISTANT)]
