class Door:
  """
  Diese Klasse beschreibt eine Türe mit der Eigenschaft
  door_is_open (für geöffnete Türe) sowie door_is_locked.
  Die Türe überwacht die beiden Zustände und verhindert.
  Das Verriegeln selber delegiert die Türe an ein Objekt.
  """

  def __init__(self, ref2door_lock, base_color):
    """
    Erzeugt ein Tür-Objekt.
    :param ref2door_lock:
    :param base_color:
    """
    self._the_door_lock = ref2door_lock
    self.color = base_color
    self._door_is_open = False
    self._door_is_locked = False

  def open_the_door(self):
    """
    Methode für das Öffnen der Türe.
    Das ist aber nur möglich, wenn die Türe nicht
    verriegelt ist.
    """
    if self._door_is_locked == False:
      self._door_is_open = True

  def close_the_door(self):
    """
    Methode für das Schließen der Türe.
    Das geht immer, auch wenn die Türe schon geschlossen ist.
    """
    self._door_is_open = False

  def lock_the_door(self):
    """
    Methode für das Verriegeln der Türe.
    Das ist nur möglich, wenn die Türe nicht offen ist.
    Für das Verriegeln ist aber das Türschloss zuständig.
    """
    if self._door_is_open == False:
      self._door_is_locked = self._the_door_lock.lock()

  def unlock_the_door(self):
    """
    Methode für das Entriegeln der Türe.
    Das ist nur möglich, wenn die Türe verriegelt ist.
    Für das Entriegeln ist aber das Türschloss zuständig.
    """
    if self._door_is_locked:
      self._door_is_locked = self._the_door_lock.unlock()

  def test(self):
    """
    Schreibt alle Attribute in den StdOut.
    """
    print(f'Türfarbe: {self.color}'
          f'\nTüre offen: {self._door_is_open}'
          f'\nTüre verriegelt: {self._door_is_locked}')

  @property
  def door_is_open(self):
    """
    Getter-Methode für den Zustand door_is_open.
    :return: True, wenn die Türe offen ist, sonst False.
    """
    return self._door_is_open

  @property
  def door_is_locked(self):
    """
    Getter-Methode für den Zustand door_is_locked.
    :return: True, wenn die Türe verriegelt ist, sonst False.
    """
    return self._door_is_locked

  @property
  def color(self):
    """
    Getter-Methode für die Eigenschaft color.
    :return: Die Farbe des Objekts.
    """
    return self._color

  @color.setter
  def color(self, new_color):
    """
    Setter-Methode für die Eigenschaft color.
    :param new_color: Neue Farbe der Türe.
    """
    self._color = new_color


class DoorLock:
  """
  Dummy-Klasse, damit in der Klasse Tür kein Fehler entsteht.
  """

  def __init__(self):
    print("Ein Schloss wurde erzeugt.")

  def lock(self):
    return True

  def unlock(self):
    return False


# Main-Methode festlegen
if __name__ == "__main__":
  print("Test für Tür-Objekt")
  the_door_lock = DoorLock()
  the_door = Door(the_door_lock, "grün")
  the_door.test()
  print("-- Türe jetzt öffnen --")
  the_door.open_the_door()
  the_door.test()
