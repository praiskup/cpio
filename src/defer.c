/* defer.c - handle "defered" links in newc and crc archives
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

#include <system.h>

#include <stdio.h>
#include <sys/types.h>
#include "cpiohdr.h"
#include "extern.h"
#include "defer.h"

struct deferment *
create_deferment (struct cpio_file_stat *file_hdr)
{
  struct deferment *d;
  d = (struct deferment *) xmalloc (sizeof (struct deferment) );
  d->header = *file_hdr;
  d->header.c_name = (char *) xmalloc (strlen (file_hdr->c_name) + 1);
  strcpy (d->header.c_name, file_hdr->c_name);
  return d;
}

void
free_deferment (struct deferment *d)
{
  free (d->header.c_name);
  free (d);
}
