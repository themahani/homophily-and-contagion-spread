#!/usr/bin/env python

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


class Network:
    """ the class that is the base for our network """
    def __init__(self, size, prob, homophily, high, low):
        # size of the network (number of agents)
        self.size = size
        # the graph object
        self.graph = np.erdos_renyi_graph(size, prob)
        # data about state and threshold of agents (in the form of hash table)
        self.agents = np.recarray((size), dtype=[('state', bool),
                                                 ('threshold', float)])
        # initial state of all agents if 0 (safe / stay at home)
        self.agents['state'] = 0
        # homophily based assignment of thresholds
        self.assign_thresholds(homophily, high, low)


    def assign_thresholds(self, homophily, high, low):
        """ use bst to assign thresholds high/low based on homophily """
        init_agent = np.random.randint(self.size)

        # begin BFS
        visited = []

        queue = [init_agent]

        while queue:
            agent = queue.pop(0)
            if agent not in visited:
                self.agents[]
                # ===================== !!! Error !!! =============
                # ======== need parent to assign threshold ========
                # =================================================
