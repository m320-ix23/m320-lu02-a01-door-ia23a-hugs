"""
This module defines the Door and DoorLock classes. The Door class represents a door with states
like open/closed and locked/unlocked, and it interacts with a DoorLock object to manage its locked state.
"""


class Door:
    """
    This class describes a door with the property 'color' and the states
    'door_is_open' (whether the door is open) and 'door_is_locked' (whether the door is locked).
    The door monitors these states to prevent invalid actions.
    Locking is delegated to an object of type DoorLock.
    """

    def __init__(self, ref2door_lock, base_color):
        """
        Initializes a Door object.

        :param ref2door_lock: Reference to a DoorLock object
        :param base_color: Initial color of the door
        """
        self._the_door_lock = ref2door_lock
        self.color = base_color
        self._door_is_open = False
        self._door_is_locked = False

    def open_the_door(self):
        """
        Opens the door if it is not locked.
        """
        if not self._door_is_locked:
            self._door_is_open = True

    def close_the_door(self):
        """
        Closes the door. This action can be performed regardless of the door's current state.
        """
        self._door_is_open = False

    def lock_the_door(self):
        """
        Locks the door if it is closed. The locking mechanism is handled by the DoorLock object.
        """
        if not self._door_is_open:
            self._door_is_locked = self._the_door_lock.lock()

    def unlock_the_door(self):
        """
        Unlocks the door if it is locked. The unlocking mechanism is handled by the DoorLock object.
        """
        if self._door_is_locked:
            self._door_is_locked = not self._the_door_lock.unlock()

    def test(self):
        """
        Outputs the current attributes of the door to the standard output.
        """
        print(f'Türfarbe: {self.color}')
        print(f'Tür offen: {self._door_is_open}')
        print(f'Tür verriegelt: {self._door_is_locked}')

    @property
    def door_is_open(self):
        """
        Returns whether the door is open.
        :return: True if the door is open, False otherwise.
        """
        return self._door_is_open

    @property
    def door_is_locked(self):
        """
        Returns whether the door is locked.
        :return: True if the door is locked, False otherwise.
        """
        return self._door_is_locked

    @property
    def color(self):
        """
        Returns the color of the door.
        :return: The color of the door.
        """
        return self._color

    @color.setter
    def color(self, new_color):
        """
        Sets a new color for the door.
        :param new_color: The new color to be applied to the door.
        """
        self._color = new_color


class DoorLock:
    """
    A simple class that represents a door lock. It provides methods to lock and unlock the door.
    """

    def __init__(self):
        """
        Initializes a DoorLock object.
        """
        print("A lock has been created.")

    def lock(self):
        """
        Locks the door.
        :return: True, indicating that the door is now locked.
        """
        return True

    def unlock(self):
        """
        Unlocks the door.
        :return: False, indicating that the door is now unlocked.
        """
        return False


# Main method for testing
if __name__ == "__main__":
    print("Testing Door object")
    the_door_lock = DoorLock()
    the_door = Door(the_door_lock, "green")
    the_door.test()
    print("-- Now opening the door")
    the_door.open_the_door()
    the_door.test()
