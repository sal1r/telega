from typing import Dict

class State:
    def __eq__(self, __value: object) -> bool:
        return True if self is type(__value) else False

class StateContext:

    def __init__(self, state: State | None) -> None:
        self.state = state
    
    def get_state(self) -> State | None:
        return self.state

    #ПЕРЕПИСАТЬ
    def set_state(self, state: State | None):
        self.state = state
    
class StateMachine:
    states: Dict[int, State]

    def set_state(self, id: int, state: State | None) -> None:
        self.states[id] = state