/* defer.h
   Copyright (C) 1993-2025 Free Software Foundation, Inc.

   This program is free software; you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation; either version 3, or (at your option)
   any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public
   License along with this program.  If not, see
   <http://www.gnu.org/licenses/>. */

struct deferment
  {
    struct deferment *next;
    struct cpio_file_stat header;
  };

struct deferment *create_deferment (struct cpio_file_stat *file_hdr);
void free_deferment (struct deferment *d);
