class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        min_deg=(minutes*6.0)

        # Calculate the angle of the hour hand
        # (Hour hand moves continuously as minutes pass)
        hour_deg=((hour+minutes/60.0)/12.0)*360
        return min(abs(min_deg - hour_deg),
           360 - abs(min_deg - hour_deg))
        
