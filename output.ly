\version "2.24.1"

bassnotes =
{
   \set Score.skipBars = ##t
   \time 4/4
   \tempo 4 = 120
   \clef bass
g4 b,4 b,1 r4 gis8 r8 gis8 r8 gis8 r8 r8 r2 c8 
}

treblenotes =
{
   \set Score.skipBars = ##t
   \time 4/4
   \tempo 4 = 120
   \clef treble
r4 r4 r1 r4 r8 r8 r8 r8 r8 r8 r8 r2 r8 
}

<<
   \new Staff \treblenotes
   \new Staff \bassnotes
>>
